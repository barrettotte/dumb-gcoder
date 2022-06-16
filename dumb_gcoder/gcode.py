import math
from typing import Optional
from .printer import Printer
from .shapes import Path

class GcodeGenerator():
    def __init__(self, printer: Printer):
        self.printer = printer
        self.src = []           # lines of GCODE source
        self.extruder = 0.0     # keep track of extruder position (absolute)
        self.cmd_padding = 38   # used to align comments
    
    def reset(self):
        self.src = []
        self.extruder = 0.0

    def gcode(self, cmd: str, comment: Optional[str] = None):
        self.src.append(cmd.ljust(self.cmd_padding) + ' ; ' + ('' if not comment else f'{comment}'))

    def line_comment(self, comment: str, aligned: bool = False):
        self.src.append(f"{(' ' * (self.cmd_padding+1)) if aligned else ''}; {comment}")

    def retract_end(self):
        self.extruder -= self.printer.retract_amount
        self.gcode(f"G1 E{self.extruder:.5f} F{self.printer.retract_speed}", "retract extruder")

    def restore_end(self):
        self.extruder += self.printer.retract_amount
        self.gcode(f"G1 E{self.extruder:.5f} F{self.printer.retract_speed}", "restore extruder position")

    def move(self, p: list[float], comment: Optional[str] = None):
        self.retract_end()
        x,y,z = f'{p[0]:.3f}', f'{p[1]:.3f}', f'{(p[2] + self.printer.z_start):.3f}'
        default_comment = f"move to ({x},{y},{z})"
        self.gcode(f"G1 X{x} Y{y} Z{z} F{self.printer.travel_speed}", default_comment if not comment else comment)
        self.restore_end()
    
    def extrude(self, a: list[float], b: list[float], thickness: Optional[int] = None, comment: Optional[str] = None):
        length = (self.printer.extruded_section * math.dist(a, b)) / self.printer.filament_section
        self.extruder += (length * (1 if not thickness else thickness))
        x,y,z = f'{b[0]:.3f}', f'{b[1]:.3f}', f'{(b[2] + self.printer.z_start):.3f}'
        default_comment = f"extrude to ({x},{y},{z})"
        self.gcode(f"G1 X{x} Y{y} Z{z} E{self.extruder:.5f}", default_comment if not comment else comment)

    def set_speed(self, f: int):
        self.gcode(f"G1 F{f}", "set speed")
    
    def set_bed_temp(self, t: int):
        self.gcode(f"M140 S{t}", "set bed temperature")
    
    def set_end_temp(self, t: int):
        self.gcode(f"M104 S{t}", "set hotend temperature")
    
    def set_positioning(self, relative: bool):
        if relative:
            self.gcode("G91", "relative mode")
        else:
            self.gcode("G90", "absolute mode")
    
    def set_fan(self, enable: bool):
        if enable:
            self.gcode("M106", "enable fan")
        else:
            self.gcode("M107", "disable fan")

    def add_prologue(self):
        self.line_comment("BEGIN prologue")
        self.gcode("M201 X500 Y500 Z100 E5000", "set max accelerations (mm/s^2))")
        self.gcode("M203 X500 Y500 Z10 E60", "set max feedrate (mm/s)")
        self.gcode("M204 P500 R1000 T500", "set P, T, and retract acceleration (mm/s^2)")
        self.gcode("M205 X8.00 Y8.00 Z0.40 E5.00", "set jerk limits (mm/s)")
        self.gcode("M205 S0 T0", "set min extrude and travel feed rate (mm/s)")
        
        self.set_fan(False)
        self.set_end_temp(self.printer.end_temp)
        self.set_bed_temp(self.printer.bed_temp)
        self.gcode(f"M190 S{self.printer.bed_temp}", "wait for bed temperature")
        self.gcode(f"M109 S{self.printer.end_temp}", "wait for hotend temperature")

        self.set_fan(False)
        self.set_positioning(False)
        self.gcode("G92 E0", "reset extruder")
        self.gcode("G28", "home XYZ")

        self.gcode(f"G1 Z2 F3000", "avoid scratching bed")
        self.gcode(f"G1 X2 Y10 Z{self.printer.z_start} F3000", "move to intro line start")
        self.gcode(f"G1 Y{self.printer.bed_size[1] - 30} Z{self.printer.z_start} E15 F1500", "intro line 1")
        self.gcode(f"G1 X2.3 Z{self.printer.z_start} F5000", "prepare for next intro line")
        self.gcode(f"G1 Y10 Z{self.printer.z_start} E30 F1200", "intro line 2")
        self.gcode("G92 E0", "reset extruder")
        self.gcode("G1 Z2 F3000", "avoid scratching bed")
        self.gcode(f"G1 X5 Y20 Z{self.printer.z_start} F5000", "prevent blob squish")
        self.gcode("G92 E0", "reset extruder")
        self.gcode("G92 E0", "reset extruder")
        self.retract_end()

        self.gcode("G21", "set units to millimeters")
        self.gcode("M82", "absolute extrusion mode")
        self.set_fan(False)
        self.line_comment("END prologue\n")

    def add_body(self, paths: list[Path]):
        self.line_comment("BEGIN body")
        self.restore_end()
        for path in paths:
            self.line_comment('new path', aligned=True)
            self.move(path.vertices[0])
            layer = int(path.vertices[0][2] / self.printer.layer_height)
            self.set_speed(self.printer.default_speed)
            
            extrusion_multiplier = 3 if layer == 1 else 1  # thicker first layer
            for i in range(len(path.vertices)-1):
                a = path.vertices[i]
                b = path.vertices[i+1]
                self.extrude(a, b, extrusion_multiplier)
        self.line_comment("END body\n")
    
    def add_epilogue(self):
        self.line_comment("BEGIN epilogue")
        self.retract_end()
        self.move([self.printer.bed_center[0], self.printer.max_y - 10, 25], "move for print removal")
        self.set_bed_temp(0)
        self.set_end_temp(0)
        self.set_fan(False)
        self.gcode("M84 X Y E", "disable motors")
        self.line_comment("END epilogue\n")

    def add_settings(self):
        self.line_comment("BEGIN settings")
        self.line_comment(f"bed_size = ({self.printer.max_x}, {self.printer.max_y}, {self.printer.max_z})")
        self.line_comment(f"bed_temp = {self.printer.bed_temp}")
        self.line_comment(f"default_speed = {self.printer.default_speed}")
        self.line_comment(f"end_temp = {self.printer.end_temp}")
        self.line_comment(f"extruder_diameter = {self.printer.extruder_diameter}")
        self.line_comment(f"filament_diameter = {self.printer.filament_diameter}")
        self.line_comment(f"layer_height = {self.printer.layer_height}")
        self.line_comment(f"retract_amount = {self.printer.retract_amount}")
        self.line_comment(f"retract_speed = {self.printer.retract_speed}")
        self.line_comment(f"travel_speed = {self.printer.travel_speed}")
        self.line_comment(f"z_start = {self.printer.z_start}")
        self.line_comment("END settings\n")

    def generate(self, paths: list[Path], out: Optional[str] = None):
        self.reset()
        self.add_prologue()
        self.add_body(paths)
        self.add_epilogue()
        self.add_settings()

        if out:
            with open(out, 'w+') as f:
                f.write('\n'.join(self.src))
        return self.src

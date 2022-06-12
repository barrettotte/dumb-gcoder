from typing import Optional
from .printer import Printer
from .shapes import Path

class GcodeGenerator():
    def __init__(self, printer: Printer):
        self.printer = printer
        self.gcode = []

    def add_gcode(self, cmd: str, comment: Optional[str] = None):
        comment = '' if not comment else f' ; {comment}'
        self.gcode.append(cmd + comment)
    
    def add_comment(self, comment: str):
        self.gcode.append(f'; {comment}')

    def add_prologue(self):
        self.add_comment("BEGIN prologue")
        # temperature set?
        # enable fans?
        self.add_gcode("G91", "relative mode")
        self.add_gcode("G1 Z1", "up 1mm")
        self.add_gcode("G28 X0 Y0", "home XY")
        self.add_gcode("G90", "absolute mode")
        self.add_gcode(f"G1 X{self.printer.bed_center[0]} Y{self.printer.bed_center[1]} F8000", "goto center")
        self.add_gcode("T0", "select extruder 1")
        self.add_gcode("G92 E0", "reset extruder position")
        self.add_comment("END prologue\n")

    def add_epilogue(self):
        self.add_comment("BEGIN epilogue")
        self.add_gcode("G91", "relative mode")
        self.add_gcode("G1 E-4 F3000", "retract filament")
        self.add_gcode(f"G1 X0 Y{self.printer.max_y}", "position for print removal")
        self.add_gcode("G1 E4", "restore filament position")
        self.add_gcode("M 107", "turn off fans")
        self.add_comment("END epilogue\n")

    def add_settings(self):
        self.add_comment("BEGIN settings")
        self.add_comment(f"bed_size = ({self.printer.max_x}mm, {self.printer.max_y}mm, {self.printer.max_z}mm)")
        self.add_comment(f"filament_diameter = {self.printer.filament_diameter}mm")
        self.add_comment(f"layer_height = {self.printer.layer_height}mm")
        self.add_comment(f"nozzle_diameter = {self.printer.nozzle_diameter}mm")
        self.add_comment("END settings\n")

    def add_body(self, paths: list[Path]):
        self.add_comment("BEGIN body")

        self.add_comment("END body\n")

    def generate(self, paths: list[Path]):
        self.add_prologue()
        self.add_body(paths)
        self.add_epilogue()
        self.add_settings()
        return self.gcode

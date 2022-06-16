import math

class Printer():
    def __init__(self, bed_size: list, extruder_diameter: float, layer_height: float, filament_diameter: float, bed_temp: int, end_temp: int, z_start: float):
        if len(bed_size) != 3:
            raise Exception("Bed size must have three dimensions [x,y,z]")

        self.bed_size = bed_size
        self.extruder_diameter = extruder_diameter
        self.layer_height = layer_height
        self.filament_diameter = filament_diameter
        self.bed_temp = bed_temp
        self.end_temp = end_temp
        self.z_start = z_start

        # derived
        self.max_x, self.max_y, self.max_z = bed_size
        self.bed_center = [self.max_x / 2.0, self.max_y / 2.0] # [x,y]
        self.extruded_section = self.extruder_diameter * self.layer_height # mm^2
        self.filament_section = math.pi * (self.filament_diameter / 2.0) ** 2  # mm^2

        # other defaults
        self.retract_speed = 5000
        self.retract_amount = 4.5
        self.default_speed = 1500
        self.travel_speed = 3000

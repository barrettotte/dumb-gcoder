import math

class Printer():
    def __init__(self, bed_size: list, nozzle_diameter: float, layer_height: float, filament_diameter: float):
        if len(bed_size) != 3:
            raise Exception("Bed size must have three dimensions [x,y,z]")
        self.bed_size = bed_size
        self.nozzle_diameter = nozzle_diameter
        self.layer_height = layer_height
        self.filament_diameter = filament_diameter

        self.max_x, self.max_y, self.max_z = bed_size
        self.bed_center = [self.max_x / 2.0, self.max_y / 2.0] # [x,y]
        self.extruded_section = self.nozzle_diameter * self.layer_height # mm^2
        self.filament_section = math.pi * (self.filament_diameter / 2.0) ** 2  # mm^2

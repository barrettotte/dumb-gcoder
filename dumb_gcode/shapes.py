import math
from typing import Optional
from .printer import Printer

class Path():
    def __init__(self):
        self.vertices = []
    
    def add_point(self, p: list[float]):
        if len(p) != 3:
            raise Exception("Points must have three dimensions [x,y,z]")
        self.vertices.append(p)
    
    def get_center(self):
        return [
            sum(v[0] for v in self.vertices) / len(self.vertices),
            sum(v[1] for v in self.vertices) / len(self.vertices),
            sum(v[2] for v in self.vertices) / len(self.vertices),
        ]

class ShapeGenerator():
    def __init__(self, printer: Printer):
        self.printer = printer
        self.paths = []

    def generate(self) -> list[Path]:
        raise NotImplementedError("Inherited Generator classes must implement generate() method")

class Cube(ShapeGenerator):
    def generate(self, side_length: float, center_x: Optional[float] = None, center_y: Optional[float] = None) -> list[Path]:
        print("Cube generating...")

        center_x = self.printer.bed_center[0] if not center_x else center_x
        center_y = self.printer.bed_center[1] if not center_y else center_y
        
        paths = []
        total_layers = side_length / self.printer.layer_height
        angle_inc = (2 * math.pi) / 4.0  # 90
        z = 0
        layer = 0

        while (layer < total_layers):
            z += self.printer.layer_height
            paths.append(Path())
            angle = 0.0
            while angle < (2 * math.pi):
                x = center_x + math.cos(angle) * side_length
                y = center_y + math.sin(angle) * side_length
                paths[-1].add_point([x,y,z])
                angle += angle_inc
            layer += 1

        # return in extrusion order (bottom to top)
        paths.sort(key=lambda x: x.get_center()[2], reverse=True)

class Square(ShapeGenerator):
    def generate(self) -> list[Path]:
        print("Square generating...")

class Circle(ShapeGenerator):
    def generate(self) -> list[Path]:
        print("Circle generating...")

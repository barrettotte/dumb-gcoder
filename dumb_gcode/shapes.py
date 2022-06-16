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

    def __repr__(self):
        return 'Path: [' + ','.join([f'({v[0]:.3f},{v[1]:.3f},{v[2]:.3f})' for v in self.vertices]) + ']'

class ShapeGenerator():
    def __init__(self, printer: Printer):
        self.printer = printer
        self.paths = []

    def generate(self) -> list[Path]:
        raise NotImplementedError("Inherited Generator classes must implement generate() method")

class Rectangle(ShapeGenerator):
    def generate(self, width: float, length: float, thickness: int) -> list[Path]:
        cx = self.printer.bed_center[0] - (width/2)
        cy = self.printer.bed_center[1] - (length/2)
        z = 0  # only one layer

        for i in range(thickness):
            p = Path()
            offset = i * (self.printer.extruder_diameter/2)
            p.add_point([0 + cx + offset, 0 + cy + offset, z])
            p.add_point([width + cx - offset, 0 + cy + offset, z])
            p.add_point([width + cx - offset, length + cy - offset, z])
            p.add_point([0 + cx + offset, length + cy - offset, z])
            p.add_point([0 + cx + offset, 0 + cy + offset, z])
            self.paths.append(p)
        return self.paths

class Square(Rectangle):
    def generate(self, length: float, thickness: int) -> list[Path]:
        return super().generate(length, length, thickness)

class Circle(ShapeGenerator):
    def generate(self) -> list[Path]:
        print("Circle generating...")
        return self.paths

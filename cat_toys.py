from dumb_gcoder.gcode import GcodeGenerator
from dumb_gcoder.printer import Printer
from dumb_gcoder.shapes import Rectangle, Square


bed_size = [220, 220, 50]
printer = Printer(bed_size, 0.4, 0.2, 1.75, 60, 210, 0.28)

gg = GcodeGenerator(printer)
gg.generate(Rectangle(printer).generate(50, 10, 5), out='shapes/rectangle.gcode')
gg.generate(Square(printer).generate(50, 5), out='shapes/square.gcode')


from dumb_gcode.gcode import GcodeGenerator
from dumb_gcode.printer import Printer
from dumb_gcode.shapes import Rectangle, Square

def main():
    bed_size = [220, 220, 50]
    printer = Printer(bed_size, 0.4, 0.2, 1.75, 60, 210, 0.3)

    gg = GcodeGenerator(printer)
    gg.generate(Rectangle(printer).generate(50, 10, 5), out='shapes/rectangle.gcode')
    gg.generate(Square(printer).generate(50, 5), out='shapes/square.gcode')

if __name__ == "__main__": main()

from dumb_gcode.gcode import GcodeGenerator
from dumb_gcode.printer import Printer
from dumb_gcode.shapes import Cube

def main():
    # TODO: get from config
    bed_size = [220, 220, 50]
    printer = Printer(bed_size, 0.4, 0.2, 1.75)
    c = Cube(printer)

    paths = c.generate(5)
    gg = GcodeGenerator(printer)
    gcode = gg.generate(paths)

    with open('test.gcode', 'w+') as f:
        f.write('\n'.join(gcode))

if __name__ == "__main__": main()

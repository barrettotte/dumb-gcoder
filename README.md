# dumb-gcoder

A dumb GCODE generator made to learn more about GCODE and 3D print my cat some basic shapes it loves to play with.

This is a dumb project so I'm only targeting the specs of my 
[Creality Ender-3 Pro](https://www.creality.com/products/ender-3-pro-3d-printer).

Maybe one day I'll try writing a small general purpose slicer.

TODO: picture of cat

I only made a square and a rectangle. I wanted to make an ellipse/circle, but I lost motivation.

```py
# cat_toys.py

from dumb_gcoder.gcode import GcodeGenerator
from dumb_gcoder.printer import Printer
from dumb_gcoder.shapes import Rectangle, Square

bed_size = [220, 220, 50]
printer = Printer(bed_size, 0.4, 0.2, 1.75, 60, 210, 0.28)

gg = GcodeGenerator(printer)

gg.generate(Rectangle(printer).generate(50, 10, 5), out='shapes/rectangle.gcode')
gg.generate(Square(printer).generate(50, 5), out='shapes/square.gcode')
```

## References

- [Marlin GCODE Reference](https://marlinfw.org/meta/gcode/)
- [PrusaSlicer G-code viewer](https://help.prusa3d.com/article/prusaslicer-g-code-viewer_193152)
- Sample GCODE
  - [slicer_examples/square_test_cura.gcode](slicer_examples/square_test_cura.gcode)
  - [slicer_examples/square_test_prusa.gcode](slicer_examples/square_test_prusa.gcode)

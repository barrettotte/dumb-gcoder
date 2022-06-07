// test square for understanding GCODE
//
// openscad -o test/square_test.stl test/square_test.scad

$fs = 0.1;
$fn = 60;

module square_unfilled(layer_height, nozzle_diameter, length, thickness) {
    printer_thickness = nozzle_diameter * thickness;
    center_cut = length - (2 * printer_thickness);

    difference() {
        cube(size=[length, length, layer_height]);

        translate([printer_thickness, printer_thickness, 0])
            cube(size=[center_cut, center_cut, layer_height]);
    }
}

square_unfilled(0.2, 0.4, 10, 3);

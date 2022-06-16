// test circle for understanding GCODE
//
// openscad -o slicer_examples/circle_test.stl slicer_examples/circle_test.scad

$fs = 0.1;
$fn = 60;

module circle_test(layer_height, nozzle_diameter, radius, thickness) {
    printer_thickness = nozzle_diameter * thickness;
    center_cut = radius - (2 * printer_thickness);

    difference() {
        cylinder(h=layer_height, r=radius, center=true);
        cylinder(h=layer_height, r=center_cut, center=true);
    }
}

circle_test(0.2, 0.4, 10, 3);

; BEGIN prologue
G91 ; relative mode
G1 Z1 ; up 1mm
G28 X0 Y0 ; home XY
G90 ; absolute mode
G1 X110.0 Y110.0 F8000 ; goto center
T0 ; select extruder 1
G92 E0 ; reset extruder position
; END prologue

; BEGIN body
; END body

; BEGIN epilogue
G91 ; relative mode
G1 E-4 F3000 ; retract filament
G1 X0 Y220 ; position for print removal
G1 E4 ; restore filament position
M 107 ; turn off fans
; END epilogue

; BEGIN settings
; bed_size = (220mm, 220mm, 50mm)
; filament_diameter = 1.75mm
; layer_height = 0.2mm
; nozzle_diameter = 0.4mm
; END settings

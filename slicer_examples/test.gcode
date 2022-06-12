G91                    ; relative mode
G1 Z1                  ; up 1mm
G28 X0 Y0              ; home X and Y axes

G90                    ; absolute mode
G1 117.5 Y125.0 F8000  ; go to center (dependent on printer bed)
G28 Z0                 ; home Z axis
G1 Z0                  ; 
T0                     ; select extruder 1
G92 E0                 ; reset extruder position

G91                    ; relative mode
G1 Z0.1                ; first layer height
G1 X5.0 Y5.0           ; start position
G1 E0.00000 F400.000   ; set speed of extrusion (slower for first layer)

; table_x = 220mm
; table_y = 220mm
; table_z = 50mm    (not used for this)

; nozzle_diameter = 0.4mm
; layer_height = 0.2mm
; filament_diameter = 1.75mm (PLA)
; path_length = 10mm

; extruded_cross_section = nozzle_diameter * layer_height = 0.8mm^2
; filament_cross_section = PI * (1.75mm/2)^2 = 2.4053mm^2

; volume_extruded_path   = extruded_cross_section * path_length = 8mm^3
; length_extruded_path   = volume_extruded_path / filament_cross_section = 10mm

G1 X-10 Y0 E0.6652

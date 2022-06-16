; BEGIN prologue
M201 X500 Y500 Z100 E5000              ; set max accelerations (mm/s^2))
M203 X500 Y500 Z10 E60                 ; set max feedrate (mm/s)
M204 P500 R1000 T500                   ; set P, T, and retract acceleration (mm/s^2)
M205 X8.00 Y8.00 Z0.40 E5.00           ; set jerk limits (mm/s)
M205 S0 T0                             ; set min extrude and travel feed rate (mm/s)
M107                                   ; disable fan
M104 S210                              ; set hotend temperature
M140 S60                               ; set bed temperature
M190 S60                               ; wait for bed temperature
M109 S210                              ; wait for hotend temperature
M107                                   ; disable fan
G90                                    ; absolute mode
G92 E0                                 ; reset extruder
G28                                    ; home XYZ
G1 Z2 F3000                            ; avoid scratching bed
G1 X2 Y10 Z0.28 F3000                  ; move to intro line start
G1 Y190 Z0.28 E15 F1500                ; intro line 1
G1 X2.3 Z0.28 F5000                    ; prepare for next intro line
G1 Y10 Z0.28 E30 F1200                 ; intro line 2
G92 E0                                 ; reset extruder
G1 Z2 F3000                            ; avoid scratching bed
G1 X5 Y20 Z0.28 F5000                  ; prevent blob squish
G92 E0                                 ; reset extruder
G92 E0                                 ; reset extruder
G1 E-4.50000 F5000                     ; retract extruder
G21                                    ; set units to millimeters
M82                                    ; absolute extrusion mode
M107                                   ; disable fan
; END prologue

; BEGIN body
G1 E0.00000 F5000                      ; restore extruder position
                                       ; path 1 of 5
G1 E-4.50000 F5000                     ; retract extruder
G1 X85.000 Y105.000 Z0.280 F3000       ; move to (85.000,105.000,0.280)
G1 E0.00000 F5000                      ; restore extruder position
G1 F1500                               ; set speed
G1 X135.000 Y105.000 Z0.280 E1.66301   ; extrude to (135.000,105.000,0.280)
G1 X135.000 Y115.000 Z0.280 E1.99561   ; extrude to (135.000,115.000,0.280)
G1 X85.000 Y115.000 Z0.280 E3.65861    ; extrude to (85.000,115.000,0.280)
G1 X85.000 Y105.000 Z0.280 E3.99122    ; extrude to (85.000,105.000,0.280)
                                       ; path 2 of 5
G1 E-0.50878 F5000                     ; retract extruder
G1 X85.200 Y105.200 Z0.280 F3000       ; move to (85.200,105.200,0.280)
G1 E3.99122 F5000                      ; restore extruder position
G1 F1500                               ; set speed
G1 X134.800 Y105.200 Z0.280 E5.64092   ; extrude to (134.800,105.200,0.280)
G1 X134.800 Y114.800 Z0.280 E5.96022   ; extrude to (134.800,114.800,0.280)
G1 X85.200 Y114.800 Z0.280 E7.60992    ; extrude to (85.200,114.800,0.280)
G1 X85.200 Y105.200 Z0.280 E7.92922    ; extrude to (85.200,105.200,0.280)
                                       ; path 3 of 5
G1 E3.42922 F5000                      ; retract extruder
G1 X85.400 Y105.400 Z0.280 F3000       ; move to (85.400,105.400,0.280)
G1 E7.92922 F5000                      ; restore extruder position
G1 F1500                               ; set speed
G1 X134.600 Y105.400 Z0.280 E9.56561   ; extrude to (134.600,105.400,0.280)
G1 X134.600 Y114.600 Z0.280 E9.87161   ; extrude to (134.600,114.600,0.280)
G1 X85.400 Y114.600 Z0.280 E11.50801   ; extrude to (85.400,114.600,0.280)
G1 X85.400 Y105.400 Z0.280 E11.81400   ; extrude to (85.400,105.400,0.280)
                                       ; path 4 of 5
G1 E7.31400 F5000                      ; retract extruder
G1 X85.600 Y105.600 Z0.280 F3000       ; move to (85.600,105.600,0.280)
G1 E11.81400 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.400 Y105.600 Z0.280 E13.43709  ; extrude to (134.400,105.600,0.280)
G1 X134.400 Y114.400 Z0.280 E13.72978  ; extrude to (134.400,114.400,0.280)
G1 X85.600 Y114.400 Z0.280 E15.35288   ; extrude to (85.600,114.400,0.280)
G1 X85.600 Y105.600 Z0.280 E15.64557   ; extrude to (85.600,105.600,0.280)
                                       ; path 5 of 5
G1 E11.14557 F5000                     ; retract extruder
G1 X85.800 Y105.800 Z0.280 F3000       ; move to (85.800,105.800,0.280)
G1 E15.64557 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.200 Y105.800 Z0.280 E17.25536  ; extrude to (134.200,105.800,0.280)
G1 X134.200 Y114.200 Z0.280 E17.53474  ; extrude to (134.200,114.200,0.280)
G1 X85.800 Y114.200 Z0.280 E19.14453   ; extrude to (85.800,114.200,0.280)
G1 X85.800 Y105.800 Z0.280 E19.42392   ; extrude to (85.800,105.800,0.280)
; END body

; BEGIN epilogue
G1 E14.92392 F5000                     ; retract extruder
G1 E10.42392 F5000                     ; retract extruder
G1 X110.000 Y210.000 Z25.280 F3000     ; move for print removal
G1 E14.92392 F5000                     ; restore extruder position
M140 S0                                ; set bed temperature
M104 S0                                ; set hotend temperature
M107                                   ; disable fan
M84 X Y E                              ; disable motors
; END epilogue

; BEGIN settings
; bed_size = (220, 220, 50)
; bed_temp = 60
; default_speed = 1500
; end_temp = 210
; extruder_diameter = 0.4
; filament_diameter = 1.75
; layer_height = 0.2
; retract_amount = 4.5
; retract_speed = 5000
; travel_speed = 3000
; z_start = 0.28
; END settings

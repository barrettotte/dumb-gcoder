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
M83                                    ; relative extrusion mode
G90                                    ; absolute mode
G28                                    ; home XYZ
G1 Z0.28                               ; avoid scratching bed with hotend
G1 X2 Y10 F3000                        ; move to intro line start
G1 Z0.28 F240                          ; avoid scratching bed
G92 E0                                 ; reset extruder position
G1 Y190 Z0.28 E15 F1500                ; intro line 1
G1 X2.3 F5000                          ; prepare for next intro line
G92 E0                                 ; reset extruder position
G1 Y10 E15 F1200                       ; intro line 2
G92 E0                                 ; reset extruder position
G21                                    ; set units to millimeters
M82                                    ; absolute extrusion mode
M107                                   ; disable fan
; END prologue

; BEGIN body
G1 E4.50000 F5000                      ; restore extruder position
                                       ; new path
G1 E0.00000 F5000                      ; retract extruder
G1 X85.000 Y85.000 Z0.280 F3000        ; move to (85.000,85.000,0.280)
G1 E4.50000 F5000                      ; restore extruder position
G1 F1500                               ; set speed
G1 X135.000 Y85.000 Z0.280 E6.16301    ; extrude to (135.000,85.000,0.280)
G1 X135.000 Y135.000 Z0.280 E7.82601   ; extrude to (135.000,135.000,0.280)
G1 X85.000 Y135.000 Z0.280 E9.48902    ; extrude to (85.000,135.000,0.280)
G1 X85.000 Y85.000 Z0.280 E11.15203    ; extrude to (85.000,85.000,0.280)
                                       ; new path
G1 E6.65203 F5000                      ; retract extruder
G1 X85.200 Y85.200 Z0.280 F3000        ; move to (85.200,85.200,0.280)
G1 E11.15203 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.800 Y85.200 Z0.280 E12.80173   ; extrude to (134.800,85.200,0.280)
G1 X134.800 Y134.800 Z0.280 E14.45143  ; extrude to (134.800,134.800,0.280)
G1 X85.200 Y134.800 Z0.280 E16.10114   ; extrude to (85.200,134.800,0.280)
G1 X85.200 Y85.200 Z0.280 E17.75084    ; extrude to (85.200,85.200,0.280)
                                       ; new path
G1 E13.25084 F5000                     ; retract extruder
G1 X85.400 Y85.400 Z0.280 F3000        ; move to (85.400,85.400,0.280)
G1 E17.75084 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.600 Y85.400 Z0.280 E19.38724   ; extrude to (134.600,85.400,0.280)
G1 X134.600 Y134.600 Z0.280 E21.02364  ; extrude to (134.600,134.600,0.280)
G1 X85.400 Y134.600 Z0.280 E22.66003   ; extrude to (85.400,134.600,0.280)
G1 X85.400 Y85.400 Z0.280 E24.29643    ; extrude to (85.400,85.400,0.280)
                                       ; new path
G1 E19.79643 F5000                     ; retract extruder
G1 X85.600 Y85.600 Z0.280 F3000        ; move to (85.600,85.600,0.280)
G1 E24.29643 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.400 Y85.600 Z0.280 E25.91953   ; extrude to (134.400,85.600,0.280)
G1 X134.400 Y134.400 Z0.280 E27.54262  ; extrude to (134.400,134.400,0.280)
G1 X85.600 Y134.400 Z0.280 E29.16572   ; extrude to (85.600,134.400,0.280)
G1 X85.600 Y85.600 Z0.280 E30.78881    ; extrude to (85.600,85.600,0.280)
                                       ; new path
G1 E26.28881 F5000                     ; retract extruder
G1 X85.800 Y85.800 Z0.280 F3000        ; move to (85.800,85.800,0.280)
G1 E30.78881 F5000                     ; restore extruder position
G1 F1500                               ; set speed
G1 X134.200 Y85.800 Z0.280 E32.39860   ; extrude to (134.200,85.800,0.280)
G1 X134.200 Y134.200 Z0.280 E34.00839  ; extrude to (134.200,134.200,0.280)
G1 X85.800 Y134.200 Z0.280 E35.61818   ; extrude to (85.800,134.200,0.280)
G1 X85.800 Y85.800 Z0.280 E37.22797    ; extrude to (85.800,85.800,0.280)
; END body

; BEGIN epilogue
G1 E32.72797 F5000                     ; retract extruder
G1 E28.22797 F5000                     ; retract extruder
G1 X110.000 Y210.000 Z25.280 F3000     ; move for print removal
G1 E32.72797 F5000                     ; restore extruder position
G1 E37.22797 F5000                     ; restore extruder position
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

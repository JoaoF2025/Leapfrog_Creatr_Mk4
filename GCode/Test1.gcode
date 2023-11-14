
;Printed @ about 0.15mm Z height, default settings

T0                               ; Select tool 0

M140 S35                         ; Set the bed temperature to 45 degrees Celsius
M105                             ; Report the current temperature of the extruder and bed
M190 S35                         ; Wait for the bed to reach 45 degrees Celsius before continuing
M104 S210                        ; Set the extruder temperature to 245 degrees Celsius
M105                             ; Report the current temperature of the extruder and bed
M109 S210                        ; Wait for the extruder to reach 245 degrees Celsius before continuing

M82                              ; Set extruder to use absolute positioning
M107                             ; Turn off the fan
M221 S100                        ; Set the flow rate percentage for the extruder motor to 100%



G92 E0                           ; Reset the extruder's position to zero
G1 E3 F100                       ; Extrude 3mm of filament at a feed rate of 100mm per minute
G92 E0                           ; Reset the extruder's position to zero again
G1 F283                          ; Set the printer's feed rate to 283mm per minute
G92 E0                           ; Reset the extruder's position to zero for the third time

M107                             ; Turn off the fan again

G0 F3600 X100 Y139.825           ; Move the print head to position X=100 and Y=139.825 at a fast speed of 3600mm per minute
G1 F1500 E0                      ; Extrude filament at a feed rate of 1500mm per minute with no movement along the X, Y, or Z axis
G1 F100 X99.858 Y139.825 E1      ; Move the print head to position X=99.858 and Y=139.825 while extruding filament at a feed rate of 60mm per minute
G1 X99.858 Y90.175 E100          ; Move the print head to position X=99.858 and Y=90.175 while extruding filament at a feed rate of 1500mm per minute to create a straight line of filament


;End G-code

G4 ; Wait
M220 S100 ; Reset Speed factor override percentage to default (100%)
M221 S100 ; Reset Extrude factor override percentage to default (100%)
M84 ; Disable stepper motors

; End of End GCode

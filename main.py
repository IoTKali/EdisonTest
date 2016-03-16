import Zone
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

exits = [(4, touch.TTP223(4))]
a = Zone.Zone(0, 20, 0, exits, lcd.Jhd1313m1(0, 0x3E, 0x62))

button = grove.GroveButton(4)
touch = touch.TTP223(8)

buttonVal = True
touchVal = True
i = 0
while True:
    if button.value() != 0 and buttonVal:
        a.checkInput()
        buttonVal = False
        i = a.getAvSpaces()
        print str(i)
    else:
        buttonVal = True
    
    if touch.isPressed() and touchVal:
        a.checkInput()
        touchVal = False
        i = a.getAvSpaces()
        print str(i)
    else:
        touchVal = True
    
    a.displayUpdate()
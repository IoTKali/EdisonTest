import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

display = lcd.Jhd1313m1(0, 0x3E, 0x62)
exitSensor = touch.TTP223(4)
regSpaces = 17
spSpaces = 5
avSpaces = regSpaces

def updateDisplay():
    display.clear()
    if avSpaces > 0:
        if avSpaces >= regSpaces / 2:
            display.setColor(0, 255, 0)
        elif avSpaces >= regSpaces / 4:
            display.setColor(255, 255, 0)
        else:
            display.setColor(255, 127, 0)
        
        display.setCursor(0, 0)
        display.write("Available spaces:")
        display.setCursor(1, 0)
        display.write(str(avSpaces))
    else:
        display.setColor(255, 0, 0)
        display.setCursor(0, 0)
        display.write("No available")
        display.setCursor(1, 0)
        display.write("places")
        
for i in range(regSpaces):
    avSpaces -= 1
    updateDisplay()
    time.sleep(1)
import time
import thread
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

display = lcd.Jhd1313m1(0, 0x3E, 0x62)
exitSensor = touch.TTP223(4)
regSpaces = 17
spSpaces = 5
inputSensor = touch.TTP223(4)
outputSensor = touch.TTP223(5)

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
        
def checkPulse(sensor):
    if sensor.isPressed():
        while True:
            if not sensor.isPressed():
                return True
    return False

avSpaces = 17

def checkExit(sensor, op):
    while True:
        if checkPulse(sensor):
            while True:
                if checkPulse(sensor):
                    if op == "add":
                        #avSpaces += 1
                    else:
                        #avSpaces -= 1
                    updateDisplay()
                    print avSpaces


#thread.start_new_thread(checkExit, (inputSensor, "add", ))
thread.start_new_thread(checkExit, (outputSensor, "sub", ))

while True:
    pass
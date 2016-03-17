def checkTouchPulse(touch):
    if touch.isPressed():
        while True:
            if not touch.isPressed():
                return True
    return False

def checkButtonPulse(button):
    if button.value() != 0:
        while True:
            if button.value() == 0:
                return True
    return False

def doubleTouchPulse(touch, op):
    while True:
        if checkTouchPulse(touch):
            while True:
                if checkTouchPulse(touch):
                    return True

def updateDisplay(display, maxSpaces, spaces):
    display.clear()
        if spaces > 0:
            if spaces >= maxSpaces / 2:
                display.setColor(0, 255, 0)
            elif spaces >= maxSpaces / 4:
                display.setColor(255, 255, 0)
            else:
                display.setColor(255, 127, 0)
                
            display.setCursor(0, 0)
            display.write("Available places:")
            display.setCursor(1, 0)
            display.write(str(spaces))
        else:
            display.setColor(255, 0, 0)
            display.setCursor(0, 0)
            display.write("No available")
            display.setCursor(1, 0)
            display.write("places")
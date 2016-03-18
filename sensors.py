import pyupm_ttp223 as ttp223
import pyupm_grove as grove

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
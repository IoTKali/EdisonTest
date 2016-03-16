import time
import mosquitto
import threading
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

class Zone:
    def __init__(self, zoneId, regSpaces, spSpaces, exits):
        self.zoneId = zoneId
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.display = lcd.Jhd1313m1(0, 0x3E, 0x62)
        self.exits = exits #exits must be an array of tuplets: (port, Zone)
        
        
    def checkExit(self, port):
        for e in self.exits:
            if e[0] == port:
                #Sends data to DB
                self.avSpaces += 1
                
    def checkInput(self):
        #Connects to DB
        self.avSpaces -= 1
        
    def displayAvailability(self):
        if self.avSpaces > 0:
            self.display.setCursor(0, 0)
            self.display.write("Available places:")
            if self.avSpaces >= self.regSpaces / 2:
                self.display.setColor(0, 255, 0)
            elif self.avSpaces >= self.regSpaces * 3 / 4:
                self.display.setColor(255, 255, 0)
            else:
                self.display.setColor(255, 127, 0)
            self.display.setCursor(1, 0)
            self.display.write(self.avSpaces)
        else:
            self.display.setCursor(0, 0)
            self.display.write("No available places")
            self.display.setColor(255, 0, 0)
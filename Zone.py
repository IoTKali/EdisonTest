import time
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
        self.exits = exits #exits must be an array of tuplets: (port, Zone)
        
    def checkExit(self, port):
        for e in self.exits:
            if e[0] == port:
                #Sends data to DB
                self.avSpaces += 1
                
    def checkInput(self):
        #Connects to DB
        self.avSpaces -= 1
        
    
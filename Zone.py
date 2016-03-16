import time
import threading
import paho.mqtt.client as mqtt
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

class Zone:
    def __init__(self, zoneId, regSpaces, spSpaces, zones, display, host):
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.exits
        self.entrances
        self.connections
        self.display = display
        
    def set_connection():
        for e in self.zones:
            #publisher(e[1])
    
    def checkExit(self, port):
        for e in self.exits:
            if e[0] == port:
                #Sends data to DB
                self.avSpaces += 1
                self.displayUpdate
                
    def checkEntrance(self):
        #Connects to DB
        self.avSpaces -= 1
        self.displayUpdate
        
    def displayUpdate(self):
        self.display.clear()
        if self.avSpaces > 0:
            if self.avSpaces >= self.regSpaces / 2:
                self.display.setColor(0, 255, 0)
            elif self.avSpaces >= self.regSpaces / 4:
                self.display.setColor(255, 255, 0)
            else:
                self.display.setColor(255, 127, 0)
                
            self.display.setCursor(0, 0)
            self.display.write("Available places:")
            self.display.setCursor(1, 0)
            self.display.write(str(self.avSpaces))
        else:
            self.display.setColor(255, 0, 0)
            self.display.setCursor(0, 0)
            self.display.write("No available")
            self.display.setCursor(1, 0)
            self.display.write("places")
            
    def getAvSpaces(self):
        return self.avSpaces
    
    def sensorChange(port):
        if ()
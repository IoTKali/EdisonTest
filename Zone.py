import time
import threading
import paho.mqtt as mqtt
import pyupm_grove as button
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

class Zone:
    def __init__(self, zoneID, regSpaces, spSpaces, inputZones, outputZones, outsideInput, outsideOutput, display, host):
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.display = display
        self.subClient = mqtt.client.Client(client_id=zoneID)
        self.subClient.connect(host)
        self.pubClients = []
        i = 0
        #¿zones?
        for e in zones:
            self.pubClients.append(mqtt.client.Client(client_id=zoneID+"_pub_"+e[1]))
            self.pubClients[i].connect(host)
            i += 1
        self.SensorIThreadArr = []
        
        
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
        
    def main():
        threadArr = []
        
    
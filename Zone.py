import threading
import SensorThread
import paho.mqtt.client as mqtt
import pyupm_grove as button
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

class Zone:
    def __init__(self, zoneID, regSpaces, spSpaces, outputZones, outsideInput, outsideOutput, display, host):
        self.zoneID = zoneID
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.display = display
        self.client = mqtt.Client(client_id=zoneID)
        self.client.connect(host)
        self.threadArr = []
        for e in outputZones:
            self.threadArr.append(SensorThread(self, e[0], e[1], self.getID()))
            
        for e in outsideInput:
            self.threadArr.append(SensorThread(self, e[0], self.zoneID, e[1]))
                                  
        for e in outsideOutput:
            self.threadArr.append(SensorThread(self, e[0], e[1], self.getID()))
        
    def on_connect(client, userdata, flags, rc):
        client.subscribe(zoneID)
        
    def on_message(client, userdata, msg):
        self.avSpaces -= 1
        self.displayUpdate()
        
    def sendMessage(self, topic, msg):
        self.client.publish(topic, msg)
        
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
        
    def getRegSpaces(self):
        return self.regSpaces
    
    def getSpSpaces(self):
       return self.spSpaces

    def getID(self):
        return self.zoneID
        
    def main():
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        for t in self.threadArr:
            t.join()
        while True:
            pass
    
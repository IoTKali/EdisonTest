import threading
import ZoneBase
import paho.mqtt.client as mqtt
import pyupm_grove as button
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch

from SensorThread import SensorThread
from sensors import displayUpdate

class Zone(ZoneBase):
    def __init__(self, zoneID, regSpaces, spSpaces, outputZones, outsideInput, outsideOutput, display, host):
        self.zoneID = zoneID
        self.regSpaces = regSpaces
        self.spSpaces = spSpaces
        self.avSpaces = regSpaces
        self.display = display
        self.client = mqtt.Client(client_id=zoneID)
        self.client.connect(host)
        self.threadArr = []
        lock = threading.Lock()
        for e in outputZones:
            o = SensorThread(self.client, e[0], e[1], self.getID(), lock)
            self.threadArr.append(o)
            
        for e in outsideInput:  
            o = SensorThread(self.client, e[0], self.getID(), e[1], lock)
            self.threadArr.append(o)
                                  
        for e in outsideOutput:
            o = SensorThread(self.client, e[0], e[1], self.getID(), lock)
            self.threadArr.append(o)
        
    def on_connect(client, userdata, flags, rc):
        client.subscribe(zoneID)
        
    def on_message(client, userdata, msg):
        self.avSpaces -= 1
        self.displayUpdate()
            
    def getAvSpaces(self):
        return self.avSpaces
        
    def getRegSpaces(self):
        return self.regSpaces
    
    def getSpSpaces(self):
       return self.spSpaces

    def getID(self):
        return self.zoneID
        
    def main(self):
        updateDisplay(self.display)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        for t in self.threadArr:
            t.start()
    
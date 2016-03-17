import threading
import sensors
import paho.mqtt.client as mqtt

class SensorThread(threading.Thread):
    def __init__(self, client, sensor, topic, msg):
        threading.Thread.__init__(self)
        self.client = client
        self.sensor = sensor
        self.topic = topic
        self.msg = msg
        
    def main(self):
        if isinstance(self.sensor, ttp223):
            if doubleTouchPulse(self.sensor):
                self.client.publish(self.topic, msg)
        else:
            if checkButtonPulse(self.sensor):
                self.client.publish(self.topic, msg)
        self.Zone.updateDisplay()
        
    def run(self):
        self.main()
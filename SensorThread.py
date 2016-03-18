import threading
import sensors
import paho.mqtt.client as mqtt

class SensorThread(threading.Thread):
    def __init__(self, client, sensor, topic, msg, lock):
        threading.Thread.__init__(self)
        self.client = client
        self.sensor = sensor
        self.topic = topic
        self.msg = msg
        self.lock = lock
        
    def main(self):
        self.lock.acquire()
        if isinstance(self.sensor, ttp223):
            if doubleTouchPulse(self.sensor):
                self.client.publish(self.topic, msg)
        else:
            if checkButtonPulse(self.sensor):
                self.client.publish(self.topic, msg)
        self.Zone.updateDisplay()
        self.lock.release()
        
    def run(self):
        self.main()
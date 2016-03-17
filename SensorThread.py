import threading
import sensors


class SensorThead(threading.Thread):
    def __init__(self, zone, sensor, topic, msg):
        threading.Thread.__init__(self)
        self.zone = zone
        self.sensor = sensor
        self.topic = topic
        self.msg = msg
        
    def main(self):
        import Zone
        if isinstance(self.sensor, ttp223):
            if doubleTouchPulse(self.sensor):
                self.Zone.sendMessage(self.topic, msg)
        else:
            if checkButtonPulse(self.sensor):
                self.Zone.sendMessage(self.topic, msg)
        self.Zone.updateDisplay()
        
    def run(self):
        self.main()
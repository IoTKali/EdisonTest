import threading
import sensors

class SensorThead(threading.Thread, Zone, sensorTopicTuple, msg):
    def __init__(self, zone, client, obj):
        threading.Thread.__init__(self)
        self.sensorTopicTuple = sensorTopicTuple
        self.msg = msg
        
    def main(self):
        if isinstance(self.sensor, ttp223):
            if doubleTouchPulse(self.sensorTopicTuple[0]):
                self.Zone.sendMessage(self.sensorTopicTuple[1], msg)
        else:
            if checkButtonPulse(self.sensor):
                self.Zone.sendMessage(self.sensorTopicTuple[1], msg)
        self.Zone.updateDisplay()
        
    def run(self):
        self.main()
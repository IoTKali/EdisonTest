import threading
#import sensors
#import pyump_ttp223 as ttp223

class SensorOThead(threading.Thread):
    def __init__(self, zone):
        threading.Thread.__init__(self)
        
    def main(self):
        if isinstance(self.sensor, ttp223):
            if doubleTouchPulse():
                client.publish(self.topic, zoneID)
        else:
            if checkButtonPulse():
                client.publish(self.topic, zoneID)
        updateDisplay() #display.updateDisplay()?
        
    def run(self):
        self.main()
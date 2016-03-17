import time
import thread
import threading
import Zone
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

#Sensor configuration
zoneID = "zone_1"
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
exitSensor = touch.TTP223(4)
regSpaces = 17
spSpaces = 5
avSpaces = regSpaces
outputZones = [(touch.TTP223(4), "zone_2")]
outsideInput =[(touch.TTP223(5), "entrance_1")]
outsideOutput = []

myZone = Zone(zoneID, regSpaces, spSpaces, outputZones, outsideInput, outsideOutput, display, host)
myZone.main()
import Zone
import time
import httplib
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

zoneID = "zone_1"
outputZones = [(touch.TTP22(4), "zone_2")]
outsideInput = [(touch.TTP(5), zoneID)]
outsideOutput = []
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
host = "10.43.28.194"

myZone = Zone(zoneID, 17, 5, outputZones, outsideInput, outsideOutput, display, host)
myZone.main()
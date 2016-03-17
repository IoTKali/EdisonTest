import Zone
import time
import httplib
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

exits = [(touch.TTP223(4), "zone_2")]
display = lcd.Jhd1313m1(0, 0x3E, 0x62) 
thisZone = Zone.Zone(0, 20, 0, exits, display)
import Zone
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

exits = [(4, touch.TTP223(4))]
a = Zone(a, 0, 20, 0, exits)

a.displayAvailability()

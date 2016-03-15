import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as touch
import pyupm_servo as servo

buttonI = grove.GroveButton(8)
buttonO = grove.GroveButton(7)

touchO = touch.TTP223(4)

display = lcd.Jhd1313m1(0, 0x3E, 0x62)

bar = servo.ES08A(5)

while True:
    print button.value()
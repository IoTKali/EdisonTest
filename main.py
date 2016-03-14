import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

for i in range(2):
    myLcd.setCursor(0,0)
    myLcd.setColor(0, 255, 0)
    myLcd.write('Disponible')
    time.sleep(2)
    myLcd.setCursor(0,0)
    myLcd.setColor(255, 0, 0)
    myLcd.write('No disponible')
    time.sleep(2)
    
myLcd.clear()
myLcd.setColor(0, 0, 0)
del myLcd
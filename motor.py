    #Copyright (C) 2016  IoT Kali

    #This program is free software; you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation; either version 2 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License along
    #with this program; if not, write to the Free Software Foundation, Inc.,
    #51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import time
import pyupm_servo as servo 

# Create the servo object using D5
gServo = servo.ES08A(5)

for i in range(0,10): 
    # Set the servo arm to 0 degrees
    gServo.setAngle(0)
    print 'Set angle to 0'
    time.sleep(1)

    # Set the servo arm to 90 degrees
    gServo.setAngle(90)
    print 'Set angle to 90'
    time.sleep(1)

    # Set the servo arm to 180 degrees
    gServo.setAngle(180)
    print 'Set angle to 180'
    time.sleep(1)

# Delete the servo object
del gServo 

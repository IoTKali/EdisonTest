import time, sys, signal, atexit
import pyupm_l298 as upmL298

# Instantiate one of the 2 possible DC motors on a L298 Dual
# H-Bridge.  For controlling a stepper motor, see the l298-stepper
# example.
myHBridge = upmL298.L298(3, 4, 7)


## Exit handlers ##
# This stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This lets you run code on exit,
# including functions from myHBridge
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)


print "Starting motor at 50% for 3 seconds..."
myHBridge.setSpeed(50)
myHBridge.setDirection(upmL298.L298.DIR_CW)
myHBridge.enable(True)

time.sleep(3)

print "Reversing direction..."
myHBridge.setDirection(upmL298.L298.DIR_NONE) # fast stop
myHBridge.setDirection(upmL298.L298.DIR_CCW)
time.sleep(3);

myHBridge.setSpeed(0)
myHBridge.enable(False)

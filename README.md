# Tamajouki

if using the 3-button USB keyboard:

1) go to params.py and change KEYBOARD_BUTTONS to True.
2) type in terminal: demsg
	the most recently plugged USB should appear last. for example:
	[11183.293196] usb 1-1.3: ch341-uart converter now attached to ttyUSB0.
3) in the game's main, update the 'port' equal in the serial port. for example:
	serial_port = serial.Serial(port="/dev/ttyUSB0", ...
	
if using mouse:
go to params.py and change KEYBOARD_BUTTONS to False.

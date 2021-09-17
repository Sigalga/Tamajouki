# Tamajouki
------------------------------------------------------------------------------------

To run the game in release mode:
Set the interpreter options to `-O`.

In debug mode the game runs with visible text, describing the stat points.

------------------------------------------------------------------------------------

If using mouse to play the game:
Do not provide any command line parameters.

------------------------------------------------------------------------------------

To use the 3-button USB keyboard:

1) Type in terminal:
	`% demsg`
	The most recently plugged-in USB should be printed last.
	for example:
	`[11183.293196] usb 1-1.3: ch341-uart converter now attached to ttyUSB0.`
	
2) In the run configuration, set the parameters to `-K <port name>`.
	for example:
	`-K /dev/ttyUSB0`

------------------------------------------------------------------------------------


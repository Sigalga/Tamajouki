# Tamajouki
Run configurations on PyCharm (Ubuntu/Windows)
------------------------------------------------------------------------------------

To run the game in release mode:
Set the interpreter options to `-O`.

In debug mode the game displays a stats board, and quick level up/down buttons.

------------------------------------------------------------------------------------

If using mouse to play the game:
Do not provide any command line parameters.

If using computer keyboard to play:
set the parameters to `-QWE`.

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


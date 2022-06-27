SETUP OF REALTIME HISTOGRAM PLOTTING CONNECTED TO ADAFRUIT CPX BOARD, FOR HISTOGRAMMING OF CPX BOARD TILT SAMPLING
1. Connect CPX board to computer via USB cable
2. Verify CPX board is running a suitable Python code:
	- ensure CPX boots at power on (says "Hello" and flashes blue LED)
        - flip switch on CPX board (if needed) and ensure CPX board starts running tilt sensing code
3. run Mu editor and ensure CPX board tilt values (0 to 9) are output to REPL display in Mu editor
	- REPL window in Mu editor is toggled on/off by clicking on "Serial" button on top row of editor
	- flip switch on CPX board and ensure CPX board ***STOPS*** running tilt sensing code
4. start running Python histogram display program from Terminal window
	- cd to .../mu_code-2022/circuitpython_kernel/examples/
	- > ./cpx-tilt-histogram-RTplotting.py
	- verify histogram graphic window appears on laptop computer screen
5. run "Atom" editor, and ensure the Atom editor has the "autosave-onchange" plugin installed, and has the computer window "focus" to receive STDIN to the editor
	- open the file "accel.csv" in .../mu_code-2022/circuitpython_kernel/examples/
	- ensure the Atom editor has the "focus" on the desktop, so that it will collect input tilt sample values to the "accel.csv" file through STDIN from the USB cable connected to the CPX board
	- NOTE: the REPL output from the CPX board is output through the USB cable to the computer and emulates STDIN from the keyboard of the computer
6. flip switch on CPX board and starting tilting the CPX board 
	- ensure CPX board starts running tilt sensing code and starts outputting values to the Atom editor session for "accel.csv"
	- ensure Python histogram display starts showing new tilt values as the large central digits, and starts incrementing the histogram plots
7. Optionally collapse and hide unwanted windows, while keeping the histogram plot window open and large for distant viewing
	- the Atom editor GUI window (while maintaining it as the "focus" window on the laptop desktop)
	- the terminal session where you are running ./cpx-tilt-histogram-RTplotting.py from the command line
	- the Mu editor window
	- any other extraneous windows
8. How to STOP the python histogram plotting session
	- kill the terminal session
	- kill the histogram graphic window
        - optionally keep a copy and then re-init the "accel.csv" file to an empty file, or having a single value






===================================================
useful code: 

e3xample09.py

data file: accel.csv

use the "atom" editor, with its autosave-onchange plugin, to add values to the file "accel.csv".

the values can be added to accel.csv if the file is in edit mode, with a live cursor at the end of file.
The values added to accel.csv can come from the Adafruit Circuit Playground Express SBC, 
with the appropriate Circuitpython code loaded and running on it.

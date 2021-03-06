
******************
Pywinauto recorder
******************

**WARNING:**
This recorder is still at a very early stage of development.


Description
###########
"Pywinauto recorder" records user interface actions and saves them in a Python script.
The generated Python script plays back user interface actions in the order in which the user recorded them.

"Pywinauto recorder" uses accessibility technologies via the Pywinauto_ library.

The functions of the generated Python script return Pywinauto wrappers so the script can be enhanced with Pywinauto
functions.

.. _Pywinauto: https://github.com/pywinauto/pywinauto/

Pywinauto_recorder.exe for Windows
##################################
"pywinauto_recorder.exe" is a standalone application, it's the compiled version for Windows.
You can download it here: Download_zip_archive_.
You just have to unzip the zip archive and then you can directly launch Pywinauto_recorder.exe.
If you drag and drop a file from the "Record files" folder to "pywinauto_recorder.exe", it will replay previously recorded user actions.

.. _Download_zip_archive: https://raw.githubusercontent.com/beuaaa/pywinauto_recorder/master/pywinauto_recorder.dist.zip

Setup
#####
 run pip install -U pywinauto_recorder (dependencies will be installed automatically)


Usage
#####

In the folder pywinauto_recorder you will find "Recorder.bat". Modify the path of the Python interpreter if necessary.

Recorder.bat:

.. code-block:: bat

    if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
    python.exe pywinauto_recorder.py

- Double click on Recorder.bat to start the recorder.
- When the recorder is started, it is in "Pause" mode.
- Press CTRL+ALT+r to switch to "Record" mode.
- If the item below the mouse cursor can be uniquely identified, it will turn green, red or blue.
- You can then click or perform another action on the user interface and the action is recorded in the generated Python script.
- Repeat this process performing a few actions on the user interface and when you're done press CTRL+ALT+r to return to "Pause" mode.
- Eventually, press CTRL+ALT+q to exit the recorder.
- The generated Python script is saved in the "Record files" folder.
- To replay a Python script, you can drag and drop it to Drag_n_drop_to_replay.bat. Modify the path of the Python interpreter if necessary.

Icons
#####

Two transparent icons are displayed at the top left of the screen:
 - the first icon corresponds to Record/Pause mode. Press CTRL+ALT+r to switch.
 - the second icon displays a green bar at each iteration of the loop. It allows you to see how fast the loop is running.

More explanations
#################

The main of "Pywinauto recorder" is an infinite loop where where at each iteration it:
 (1) finds the path of the element under the mouse cursor. The path is formed by the window_text and control_type pair of the element and all its ancestors.
 (2) searches for an unambiguous path, if found, it colors the element region green or orange.
 (3) records a user action in a file involving the last recognized unique path.

.. note::  The mouse coordinates recorded are relative to the center of the element recognized with a unique path.

If the path of the element under the mouse cursor is not ambiguous, the region of the element is colored green. Otherwise two strategies are used to try to disambiguate the path in the following order:
 (1) All elements having the same path are ordered in a 2D array. The path of the element region under the mouse cursor is disambiguated by adding a row index and a column index so that it is colored orange. The other element regions are colored red
 (2) An element whose path is unambiguous is searched on the same line on the left, if found its region is colored blue and the element under the mouse cursor is colored orange.

Functions
**********************

To be completed

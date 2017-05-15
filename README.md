# RGDCArcadeFrontend
RGDC Arcade Machine
---
---
This is the front-end for the arcade machine created by the RIT Game Development Club. Features:
- Game selection screen with sorting, filters, and a search function
- Accessing game metadata through XML files
- Launching game executables
- Returning to the game selection screen when a game closes
- Starting up automatically in place of the usual Windows boot sequence

USEFUL RESOURCES:
https://github.com/Stents-/XOutput/releases/tag/v0.11
http://www.xgameroom.com/service/ServiceFiles/XOutput.ini
http://www.headsoft.com.au/index.php?category=vjoy
http://www.xgameroom.com/service/ServiceFiles/X-Arcade.ini
https://support.xgaming.com/support/solutions/articles/12000003227-use-x-arcade-as-a-windows-joystick-gamepad-controller-xinput-
https://downloads.sourceforge.net/project/pywin32/pywin32/Build216/README.txt?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2F&ts=1494374073&use_mirror=svwh

REQUIRES:
- pygame
- most recent pip version
- win32api (https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)
- VJoy
- XOutput
- python 3.6.1

FUTURE THOUGHTS:
http://www.blendedtechnologies.com/realtime-plot-of-arduino-serial-data-using-python
etc...


# How to Install Pygame on Windows 10

Download Python 3.6.1 or greater from [Python.org](https://www.python.org/)

Run the `python-3.6.1.exe`, and make sure that you check the "Create Enviornment Variables" option. 

Open up command prompt, or powershell AS ADMIN (Right click on it in windows and click 'Run As Administrator')

Type the following commands to install Pygame:
`pip install pygame --user`

Type the following commands to install pipwin32:
`pip install pypiwin32`

Now you have pygame installed and are ready to go! To start the front end of this project, go to the folder that you have downloaded it to, and run `main.py`.  


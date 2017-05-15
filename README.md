# Features:
- Game selection screen with sorting, filters, and a search function
- Accessing game metadata through XML files
- Launching game executables
- Returning to the game selection screen when a game closes
- Starting up automatically in place of the usual Windows boot sequence

# Requirements:
- pygame
- pip
- win32api 
- VJoy
- XOutput
- python 3.6.1

# How to Install Pygame on Windows 10

Download Python 3.6.1 or greater from [Python.org](https://www.python.org/)

Run the `python-3.6.1.exe`, and make sure that you check the "Create Enviornment Variables" option. 

Open up command prompt, or powershell AS ADMIN (Right click on it in windows and click 'Run As Administrator')

Type the following commands to install Pygame:
`pip install pygame --user`

Type the following commands to install pipwin32:
`pip install pypiwin32`

Now you have pygame installed and are ready to go! To start the front end of this project, go to the folder that you have downloaded it to, and run `main.py`.  

***

# Future thoughts...
[Using and Arduino for input](http://www.blendedtechnologies.com/realtime-plot-of-arduino-serial-data-using-python)

***

# Useful Resources:
[Python Official](https://www.python.org/download/releases/3.0/)

[Getting started with Pygame](https://www.pygame.org/wiki/GettingStarted)

[XOutput](https://github.com/Stents-/XOutput/releases/tag/v0.11)

[X game room](http://www.xgameroom.com/service/ServiceFiles/XOutput.ini)

[Headsoft, VJoy](http://www.headsoft.com.au/index.php?category=vjoy)

[X Arcade fomr X Gameroom](http://www.xgameroom.com/service/ServiceFiles/X-Arcade.ini)

[X Gameroom, using a windows joystick](https://support.xgaming.com/support/solutions/articles/12000003227-use-x-arcade-as-a-windows-joystick-gamepad-controller-xinput-)

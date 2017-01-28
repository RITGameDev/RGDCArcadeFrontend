
import subprocess
import os, sys

class GameManager():
    def LaunchGame(gameData):
        print("Launching " + str(gameData["Meta"]["Title"]))

        # Get this script's filepath
        oldCwd = os.getcwd()
        thisPath = ""
        try:
            thisPath = os.path.dirname(os.path.abspath(__file__))
        except:
            print("[ERROR GAMEMANAGER.PY] Couldn't get filepath: " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))
            return

        # Get the executable file's path
        gameFolderPath = thisPath + "\\..\\games\\" + gameData["Meta"]["Folder Name"]
        executableRelativePath = gameData["FilePaths"]["Executable"]
        executableAbsolutePath = gameFolderPath + "\\game\\" + executableRelativePath

        # Add the game folder to the working directory
        addDirectoryPath = gameFolderPath + "\\game"
        sys.path.append(addDirectoryPath)
        os.chdir(addDirectoryPath)
        print("Set os.getcwd() to " + str(addDirectoryPath))

        # Run the game's executable file
        try:
            # Try to run as a Win32 executable in a separate process
            process = subprocess.Popen(threading.current_thread().exePath, stdout=subprocess.PIPE)#, creationflags=0x08000000) #creationflags=0x08000000 suppresses the launch of a window
            process.wait()
            #os.system(executableAbsolutePath)
        except:
            #print("[ERROR HOME.PY] Error running game as Win32 executable: " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))
            try:
                # Try to run by opening as a python script or other file
                os.system(executableAbsolutePath)
            except:
                print("[ERROR HOME.PY] Error running game: " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))

        # Finished running game
        print("Finished running " + str(gameData["Meta"]["Title"]))
        os.chdir(oldCwd)

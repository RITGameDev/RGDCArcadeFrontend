# RGDC Arcade Machine Frontend

# Import modules
import os.path

# Read the XML file that contains information about the game
def ReadGameData(UntangleXML, gameFolderName):
    # Set file path
    fileName = 'games/' + gameFolderName + '/info.xml'

    # Check if file exists
    if os.path.exists(fileName):
        # Parse the XML data
        info = UntangleXML(fileName)

        # Put the game information into a dict
        gameData = {
            'Meta': {
                'Title': str(info.game.meta.title.cdata).strip(),
                'Author': str(info.game.meta.author.cdata).strip(),
                'Description': str(info.game.meta.description.cdata).strip(),
                'Genres': [genre['id'].upper() for genre in info.game.meta.genres.genre]
                },
            'FilePaths': {
                'Thumbnail': str(info.game.filepaths.thumbnail.cdata).strip(),
                'Executable': str(info.game.filepaths.executable.cdata).strip()
                }
        }

        # Return game information as a dict
        return gameData
    
    else:
        # The information file could not be found
        print('[ERROR] [' + gameFolderName + '] Game information file does not exist!')
        return None

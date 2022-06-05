from .image import Image , GIF
from .exceptions import InvalidAction , SongNotFound

import requests

class Song:
    '''
    Represents a song.\n

    `Song,title` - Name of the song\n
    `Song.author` - Author of the song\n
    `Song.lyrics` - Lyrics of the song\n
    `Song.thumbnail` - Thumbnail of the song\n
    `Song.save_lyrics()` - Saves the lyrics in a text file.
    '''
    def __init__(self , x: dict):
        self.raw_data = x

    @property
    def title(self):
        '''
        Name of the song
        '''
        return self.raw_data['title']

    @property
    def author(self):
        '''
        Author of the song
        '''
        return self.raw_data['author']

    @property
    def lyrics(self):
        '''
        Lyrics of the song
        '''
        return self.raw_data['lyrics']

    @property
    def thumbnail(self):
        '''
        Tumbnail of the song
        '''
        return Image(self.raw_data['thumbnail'])

    def save_lyrics(self , filename=None):
        """
        Saves the lyrics of the song in a text file.

        :param filename: Name of the file where the lyrics should be saved. Saves in the file with the name of the song if None.
        """
        if filename is None:
            print(self.lyrics , file=open(f'{self.title}.txt' , 'w'))
        else:
        	print(self.lyrics , file=open(filename , "w"))

S = "https://some-random-api.ml/"
ANIME = S+"animu/"

class MiscClient:
    """Represents a client for anime related and misc endpoints\n

    `MiscClient.anime(action: str)` - Get an animated gif for the requested action\n
    `MiscClient.lyrics(song_name: str , cancerL str = None)` - Get the lyrics of the requested song
    """

    def __init__(self):
        self.session = requests.session()

    def anime(self , action: str):
        """Gets an animated GIF of the provided action\n

        :param action: Action of the GIF. [wink , pat , hug]\n
        :raises InvalidAction: Raises `InvalidAction` when the action provided is not available\n
        :return: The animated GIF\n
        :rtype: GIF
        """
        try:
            r = self.session.get(ANIME+action.lower()).json()
            return GIF(r['link'])
        except:
            raise InvalidAction(f"Action '{action.lower()}' was not found. Available actions - wink , hug , pat")

    def lyrics(self , song_name: str , cancer: str = None):
        """Gets the lyrics of the song requested.\n

        :param action: Action of the GIF. [wink , pat , hug]\n
        :raises SongNotFound: Raises `SongNotFound` if the requested song was not found.\n
        :return: Info about the song with lyrics
        :rtype: Song
        """

        if cancer is None:
            r = self.session.get(S+"lyrics?title="+song_name.replace(' ' , '%20')).json()
        else:
            r = self.session.get(S+"lyrics?title="+song_name.replace(' ' , '%20')+"&cancer="+cancer).json()

        if "error" in r:
            raise SongNotFound(f"Song '{song_name}' was not found.")
        else:
            return Song(r)
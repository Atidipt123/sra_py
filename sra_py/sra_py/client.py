from .canvas import CanvasClient
from .animal import AnimalClient
from .misc import MiscClient

class Client:
    """\n
    The client for all endpoints.\n

    `Client.canvas` - For canvas related endpoints\n
    `Client.animal` - For animal related endpoints
    """

    def __init__(self):
        self.canvas = CanvasClient()
        self.animal = AnimalClient()
        self.misc = MiscClient()

    @property
    def version(self):
        '''
        Version of the client
        '''

        return '1.0'

    def close(self):
        '''
        Logs out from the website.
        '''

        self.canvas.session.close()
        self.animal.session.close()
        self.misc.session.close()
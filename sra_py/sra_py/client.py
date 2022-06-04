from .canvas import CanvasClient
from .animal import AnimalClient

class Client:
    """\n
    The client for all endpoints.\n

    `Client.canvas` - For canvas related endpoints\n
    `Client.animal` - For animal related endpoints
    """

    def __init__(self):
        self.canvas = CanvasClient()
        self.animal = AnimalClient()

    def close(self):
        '''
        Logs out from the website.
        '''

        self.canvas.session.close()
        self.animal.session.close()
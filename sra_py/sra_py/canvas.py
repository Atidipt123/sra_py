import requests

from .image import Image
from .exceptions import EndpointNotFound

CANVAS = "https://some-random-api.ml/canvas/"

class CanvasClient:
    """Represents a client for canvas related endpoints\n

    `CanvasClient.pixelate(image_url: str , key: str = None)` - Pixelate an image
    """

    def __init__(self):
        self.session = requests.session()

    def pixelate(self , image_url: str , key: str = None) -> Image:
        """Pixelate an image

        :param image_url: URL of the image
        :param key: premium key, defaults to None
        :return: Pixelated  Image
        :rtype: Image
        """

        if key is not None:
            return Image(CANVAS+'pixelate?avatar='+image_url+'&key='+key)
        else:
            return Image(CANVAS+'pixelate?avatar='+image_url)

    def blur(self , image_url: str , key: str = None) -> Image:
        """Blur an image

        :param image_url: URL of the image
        :param key: premium key, defaults to None
        :return: Blurred  Image
        :rtype: Image
        """

        if key is not None:
            return Image(CANVAS+'blur?avatar='+image_url+'&key='+key)
        else:
            return Image(CANVAS+'blur?avatar='+image_url)

    def youtube_comment(self , avatar_url: str , username: str , comment: str , key: str = None):
        """Fake YouTube Comment

        :param avatar_url: Avatar of the commenting user
        :param username: Username of the commenting user
        :param comment: The comment
        :param key: Premium Key, defaults to None
        :return: The Comment Image
        :rtype: Image
        """



        if key is not None:
            return Image(CANVAS+'youtube-comment?avatar='+avatar_url+'&username='+username+'&comment='+comment+'&key=key')
        else:
            return Image(CANVAS+'youtube-comment?avatar='+avatar_url+'&username='+username+'&comment='+comment)

    def tweet(self , avatar_url: str , username: str, display_name: str , tweet_content: str , key: str = None):
        """Fake tweet

        :param avatar_url: Avatar of the tweet's author
        :param username: Username of the tweet's author
        :param display_name: Display Name of the tweet's author
        :param tweet_content: The content of the tweet
        :param key: Premium Key, defaults to None
        :return: The tweet image
        :rtype: Image
        """
        if key is not None:
            return Image(CANVAS+'tweet?avatar='+avatar_url+'&username='+username+'&displayname='+display_name+'&comment='+tweet_content+'&key='+key)
        else:
            return Image(CANVAS+'tweet?avatar='+avatar_url+'&username='+username+'&displayname='+display_name+'&comment='+tweet_content)

    def greyscale(self , image_url: str , key: str=None):
        """Apply greyscale filter to an image

        :param image_url: The url of the image
        :param key: Premium Key, defaults to None
        :return: Greyscale image
        :rtype: Image
        """
        if key is not None:
            return Image(CANVAS+'greyscale?avtar='+image_url+'&key='+key)
        else:
            return Image(CANVAS+'greyscale?avtar='+image_url)

    def invert(self , image_url: str , key: str=None):
        """Apply invert filter to an image

        :param image_url: The url of the image
        :param key: Premium Key, defaults to None
        :return: Inverted image
        :rtype: Image
        """
        if key is not None:
            return Image(CANVAS+'invert?avtar='+image_url+'&key='+key)
        else:
            return Image(CANVAS+'invert?avtar='+image_url)
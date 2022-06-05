import requests
import re

from .exceptions import DownloadError

class Image:
    """Represents an Image.\n

    `Image.image_url` - URL of the image\n
    `Image.save()` - Save the image
    """

    def __init__(self , image_url: str):
        self.image_url_ = image_url

    @property
    def image_url(self):
        """The URL of the image

        :return: Image Url
        :rtype: str
        """
        return self.image_url_

    def save(self , filename: str = None) -> None:
        """Saves the image
        :param filename: The filename where the image should download, defaults to None
        :raises DownloadError: Raises `DownloadError` if the download fails.
        :return: None
        """
        if filename is None or not filename.endswith('.png') and not filename.endswith('.jpg'):
            filename = self.image_url.split('/')[-1]

        try:
            
            r = requests.get(self.image_url , allow_redirects = True)
            open(filename , 'wb').write(r.content)
            return None
        except:
            raise DownloadError('Could not download the image')

class GIF(Image):
    """
    Represents a GIF.\n

    `GIF.image_url` - URL of the GIF\n
    `GIF.save()` - Save the GIF. 
    """

    pass
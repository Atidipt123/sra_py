import requests

from .image import Image
from .exceptions import EndpointNotFound

URL = "https://some-random-api.ml/animal/"

class AnimalClient:
    """The Client for Animal Related endpoints.\n

    `AnimalCient.get_endpoint(endpoint)` - Fetch an endpoint\n
    `AnimalCient.get_image(animal)` - Get an image of the animal\n
    `AnimalCient.get_fact(animal)` - Get a fact related to the animal
    """
    def __init__(self):
        self.session = requests.session()

    def get_endpoint(self , endpoint: str) -> dict:
        """Fetches an endpoint and returns the JSON data.

        :param endpoint: The endpoint you want to fetch.
        :raises EndpointNotFound: Raises `EndpointNotFound` when the requested endpoint is not found.
        :return: The JSON data
        :rtype: dict
        """
        try:
            f = self.session.get(URL+endpoint)
            return f.json()
        except:
            raise EndpointNotFound(f"Could not fetch the endpoint \'{endpoint}\' ({URL+endpoint})")

    def get_image(self , animal: str) -> Image:
        """Get an image of the animal

        :param animal: The animal you want the image of.
        :return: The image of the image
        :rtype: Image
        """

        return Image(self.get_endpoint(animal)['image'])

    def get_fact(self , animal: str) -> str:
        """Similar to `AnimalClent.get_image()`, this returns a random fact about the animal.

        :param animal: The animal you want the fact of.
        :return: The fact of the animal
        :rtype: str
        """

        return self.get_endpoint(animal)['fact']
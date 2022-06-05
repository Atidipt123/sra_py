class EndpointNotFound(Exception):
    """Exception raised when the requested endpoint is not found.
    """
    pass

class DownloadError(Exception):
    """Exception raised when the image failed to download
    """
    pass

class RequiresPremium(Exception):
    """Exception raised when a premium endpoint is fetched without providing a premium key.
    """
    pass

class InvalidAction(Exception):
    """
    Exception raised when an invalid action endpoint is requested.
    """

class SongNotFound(Exception):
    """
    Exception raised when the requested song was not found.
    """
"""Response code"""

from enum import Enum


class ResponseCode(Enum):
    """
    Enum for system response codes.
    """

    def __init__(self, code, msg):
        """
        Initialize a system response code.

        Args:
            code (int): The response code.
            msg (str): The response message.
        """
        self.code = code
        self.msg = msg

    SUCCESS = (0, "Success")
    SERVICE_INTERNAL_ERROR = (-1, "Service internal error")

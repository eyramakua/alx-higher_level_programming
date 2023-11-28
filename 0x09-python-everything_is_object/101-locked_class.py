#!/usr/bin/python3
"""Creates a class LockedClass"""


class LockedClass:
    """
    Prevents user from dynamically creating new attributes,
    except if the new instance attribute is first_name.
    Attributes:
        first_name (str): first name of a thing
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of LockedClass"""

        self.first_name = "first_name"

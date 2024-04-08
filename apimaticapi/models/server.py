# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Server(object):

    """Implementation of the 'Server' model.

    The user can specify multiple servers within an environment. A server
    comprises of a name and a URL. The names of the hosts remain consistent
    over different environments but their values may vary. The URL values can
    contain any number of parameters defined.

    Attributes:
        id (str): Unique Server identifier
        name (str): Server Name
        url (str): Server URL

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "url": 'url'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 url=None):
        """Constructor for the Server class"""

        # Initialize members of the class
        self.id = id 
        self.name = name 
        self.url = url 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        # Return an object of this model
        return cls(id,
                   name,
                   url)

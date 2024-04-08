# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GenerateOnPremPortalViaBuildInputRequestBody(object):

    """Implementation of the 'GenerateOnPremPortalViaBuildInputRequestBody' model.

    TODO: type model description here.

    Attributes:
        file (binary): The input file to the Portal Generator. Must contain
            the build file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file": 'file'
    }

    def __init__(self,
                 file=None):
        """Constructor for the GenerateOnPremPortalViaBuildInputRequestBody class"""

        # Initialize members of the class
        self.file = file 

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
        file = dictionary.get("file") if dictionary.get("file") else None
        # Return an object of this model
        return cls(file)

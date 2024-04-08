# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UserCodeGenerationRequirements(object):

    """Implementation of the 'UserCodeGenerationRequirements' model.

    TODO: type model description here.

    Attributes:
        user_id (str): Unique User Identifier
        input_file (str): API Specification file in a supported format

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": 'userId',
        "input_file": 'inputFile'
    }

    def __init__(self,
                 user_id=None,
                 input_file=None):
        """Constructor for the UserCodeGenerationRequirements class"""

        # Initialize members of the class
        self.user_id = user_id 
        self.input_file = input_file 

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
        user_id = dictionary.get("userId") if dictionary.get("userId") else None
        input_file = dictionary.get("inputFile") if dictionary.get("inputFile") else None
        # Return an object of this model
        return cls(user_id,
                   input_file)

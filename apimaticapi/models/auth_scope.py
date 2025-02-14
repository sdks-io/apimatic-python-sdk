# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AuthScope(object):

    """Implementation of the 'AuthScope' model.

    TODO: type model description here.

    Attributes:
        id (str): Scope Id
        name (str): Scope Name
        value (str): Scope Value
        description (str): Scope Description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "value": 'value',
        "description": 'description'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 value=None,
                 description=None):
        """Constructor for the AuthScope class"""

        # Initialize members of the class
        self.id = id 
        self.name = name 
        self.value = value 
        self.description = description 

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
        value = dictionary.get("value") if dictionary.get("value") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        # Return an object of this model
        return cls(id,
                   name,
                   value,
                   description)

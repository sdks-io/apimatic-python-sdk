# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TransformViaUrlRequest(object):

    """Implementation of the 'TransformViaUrlRequest' model.

    This structure puts together the URL of the file to be transformed, along
    with the desired export format.

    Attributes:
        url (str): The URL for the API specification file.<br><br>**Note:**
            This URL should be publicly accessible.
        export_format (ExportFormats): The structure contains API
            specification formats that Transformer can convert to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "export_format": 'export_format'
    }

    def __init__(self,
                 url=None,
                 export_format=None):
        """Constructor for the TransformViaUrlRequest class"""

        # Initialize members of the class
        self.url = url 
        self.export_format = export_format 

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
        url = dictionary.get("url") if dictionary.get("url") else None
        export_format = dictionary.get("export_format") if dictionary.get("export_format") else None
        # Return an object of this model
        return cls(url,
                   export_format)

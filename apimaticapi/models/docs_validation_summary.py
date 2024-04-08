# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DocsValidationSummary(object):

    """Implementation of the 'DocsValidationSummary' model.

    TODO: type model description here.

    Attributes:
        success (bool): TODO: type description here.
        errors (List[str]): TODO: type description here.
        warnings (List[str]): TODO: type description here.
        messages (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "success": 'success',
        "errors": 'errors',
        "warnings": 'warnings',
        "messages": 'messages'
    }

    def __init__(self,
                 success=None,
                 errors=None,
                 warnings=None,
                 messages=None):
        """Constructor for the DocsValidationSummary class"""

        # Initialize members of the class
        self.success = success 
        self.errors = errors 
        self.warnings = warnings 
        self.messages = messages 

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
        success = dictionary.get("success") if "success" in dictionary.keys() else None
        errors = dictionary.get("errors") if dictionary.get("errors") else None
        warnings = dictionary.get("warnings") if dictionary.get("warnings") else None
        messages = dictionary.get("messages") if dictionary.get("messages") else None
        # Return an object of this model
        return cls(success,
                   errors,
                   warnings,
                   messages)

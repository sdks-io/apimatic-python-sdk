# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TestGenSettings(object):

    """Implementation of the 'TestGenSettings' model.

    This structure helps specify additional test configurations which affects
    how test cases are generated.

    Attributes:
        precision_delta (float): Error margin for comparing values in decimal
            places
        test_timeout (int): Number of seconds after which if the endpoint is
            not returning any response, the test is forced to fail e.g. a
            timeout of 60
        configuration (object): The parameters allows to provide values for
            configuration file for use in the test environment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "precision_delta": 'precisionDelta',
        "test_timeout": 'testTimeout',
        "configuration": 'configuration'
    }

    def __init__(self,
                 precision_delta=None,
                 test_timeout=None,
                 configuration=None):
        """Constructor for the TestGenSettings class"""

        # Initialize members of the class
        self.precision_delta = precision_delta 
        self.test_timeout = test_timeout 
        self.configuration = configuration 

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
        precision_delta = dictionary.get("precisionDelta") if dictionary.get("precisionDelta") else None
        test_timeout = dictionary.get("testTimeout") if dictionary.get("testTimeout") else None
        configuration = dictionary.get("configuration") if dictionary.get("configuration") else None
        # Return an object of this model
        return cls(precision_delta,
                   test_timeout,
                   configuration)

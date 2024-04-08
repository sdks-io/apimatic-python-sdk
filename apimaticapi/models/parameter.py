# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from apimaticapi.models.attributes import Attributes


class Parameter(object):

    """Implementation of the 'Parameter' model.

    Parameters are options passed with the endpoint

    Attributes:
        optional (bool): If parameter is optional
        mtype (str): Type of Parameter
        constant (bool): IF Parameter is constant
        is_array (bool): If Param is collected as array
        is_stream (bool): TODO: type description here.
        is_attribute (bool): TODO: type description here.
        is_map (bool): TODO: type description here.
        attributes (Attributes): The structure contain attribute details of a
            parameter type.
        nullable (bool): If Parameter is nullable
        id (str): Unique Parameter identifier
        name (str): Parameter Name
        description (str): Parameter Description
        default_value (str): Default Values of a Parameter
        param_format (str): Specify Parameter Format

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "optional": 'optional',
        "mtype": 'type',
        "constant": 'constant',
        "is_array": 'isArray',
        "is_stream": 'isStream',
        "is_attribute": 'isAttribute',
        "is_map": 'isMap',
        "attributes": 'attributes',
        "nullable": 'nullable',
        "id": 'id',
        "name": 'name',
        "description": 'description',
        "default_value": 'defaultValue',
        "param_format": 'ParamFormat'
    }

    def __init__(self,
                 optional=None,
                 mtype=None,
                 constant=None,
                 is_array=None,
                 is_stream=None,
                 is_attribute=None,
                 is_map=None,
                 attributes=None,
                 nullable=None,
                 id=None,
                 name=None,
                 description=None,
                 default_value=None,
                 param_format=None):
        """Constructor for the Parameter class"""

        # Initialize members of the class
        self.optional = optional 
        self.mtype = mtype 
        self.constant = constant 
        self.is_array = is_array 
        self.is_stream = is_stream 
        self.is_attribute = is_attribute 
        self.is_map = is_map 
        self.attributes = attributes 
        self.nullable = nullable 
        self.id = id 
        self.name = name 
        self.description = description 
        self.default_value = default_value 
        self.param_format = param_format 

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
        optional = dictionary.get("optional") if "optional" in dictionary.keys() else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        constant = dictionary.get("constant") if "constant" in dictionary.keys() else None
        is_array = dictionary.get("isArray") if "isArray" in dictionary.keys() else None
        is_stream = dictionary.get("isStream") if "isStream" in dictionary.keys() else None
        is_attribute = dictionary.get("isAttribute") if "isAttribute" in dictionary.keys() else None
        is_map = dictionary.get("isMap") if "isMap" in dictionary.keys() else None
        attributes = Attributes.from_dictionary(dictionary.get('attributes')) if dictionary.get('attributes') else None
        nullable = dictionary.get("nullable") if "nullable" in dictionary.keys() else None
        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        default_value = dictionary.get("defaultValue") if dictionary.get("defaultValue") else None
        param_format = dictionary.get("ParamFormat") if dictionary.get("ParamFormat") else None
        # Return an object of this model
        return cls(optional,
                   mtype,
                   constant,
                   is_array,
                   is_stream,
                   is_attribute,
                   is_map,
                   attributes,
                   nullable,
                   id,
                   name,
                   description,
                   default_value,
                   param_format)

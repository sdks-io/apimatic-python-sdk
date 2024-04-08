# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from apimaticapi.api_helper import APIHelper


class APIEntityCodeGeneration(object):

    """Implementation of the 'APIEntityCodeGeneration' model.

    The Code Generation structure encapsulates all the  the details of an SDK
    generation performed against an API Entity

    Attributes:
        id (str): Unique Code Generation Identifier
        template (Platforms): The structure contains platforms that APIMatic
            CodeGen can generate SDKs and Docs in.
        generated_file (str): The generated SDK
        generated_on (datetime): Generation Date and Time
        hash_code (str): The md5 hash of the API Description
        code_generation_source (str): Generation Source
        code_gen_version (str): Generation Version
        success (bool): Generation Status
        api_entity_id (str): Unique API Entity Identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "template": 'template',
        "generated_file": 'generatedFile',
        "generated_on": 'generatedOn',
        "hash_code": 'hashCode',
        "code_generation_source": 'codeGenerationSource',
        "code_gen_version": 'codeGenVersion',
        "success": 'success',
        "api_entity_id": 'apiEntityId'
    }

    def __init__(self,
                 id=None,
                 template='CS_NET_STANDARD_LIB',
                 generated_file=None,
                 generated_on=None,
                 hash_code=None,
                 code_generation_source=None,
                 code_gen_version=None,
                 success=None,
                 api_entity_id=None):
        """Constructor for the APIEntityCodeGeneration class"""

        # Initialize members of the class
        self.id = id 
        self.template = template 
        self.generated_file = generated_file 
        self.generated_on = APIHelper.apply_datetime_converter(generated_on, APIHelper.RFC3339DateTime) if generated_on else None 
        self.hash_code = hash_code 
        self.code_generation_source = code_generation_source 
        self.code_gen_version = code_gen_version 
        self.success = success 
        self.api_entity_id = api_entity_id 

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
        template = dictionary.get("template") if dictionary.get("template") else 'CS_NET_STANDARD_LIB'
        generated_file = dictionary.get("generatedFile") if dictionary.get("generatedFile") else None
        generated_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("generatedOn")).datetime if dictionary.get("generatedOn") else None
        hash_code = dictionary.get("hashCode") if dictionary.get("hashCode") else None
        code_generation_source = dictionary.get("codeGenerationSource") if dictionary.get("codeGenerationSource") else None
        code_gen_version = dictionary.get("codeGenVersion") if dictionary.get("codeGenVersion") else None
        success = dictionary.get("success") if "success" in dictionary.keys() else None
        api_entity_id = dictionary.get("apiEntityId") if dictionary.get("apiEntityId") else None
        # Return an object of this model
        return cls(id,
                   template,
                   generated_file,
                   generated_on,
                   hash_code,
                   code_generation_source,
                   code_gen_version,
                   success,
                   api_entity_id)

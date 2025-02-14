# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimaticapi.api_helper import APIHelper
from apimaticapi.configuration import Server
from apimaticapi.utilities.file_wrapper import FileWrapper
from apimaticapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from apimaticapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.configurations.endpoint_configuration import EndpointConfiguration
from apimaticapi.exceptions.api_exception import APIException


class DocsPortalManagementController(BaseController):

    """A Controller to access Endpoints in the apimaticapi API."""
    def __init__(self, config):
        super(DocsPortalManagementController, self).__init__(config)

    def publish_hosted_portal(self,
                              api_entity_id):
        """Does a PUT request to /api-entities/{api_entity_id}/hosted-portal.

        Publish artifacts for a Hosted Portal.
        This endpoint regenerates all the artifacts for a hosted portal and
        uploads them to APIMatic's cloud storage, from where the Portal
        fetches them. These artifacts include:
        1. SDKs
        2. Docs
        3. API Specification files
        Call this endpoint to update your Hosted Portal after you update an
        API Entity via any of the Import API Endpoints.
        __**Note: If you have an embedded portal against the same API Entity,
        artifacts for that portal will get updated as well.**__

        Args:
            api_entity_id (str): The ID of the API Entity to update the portal
                artifacts for.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api-entities/{api_entity_id}/hosted-portal')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('api_entity_id')
                            .value(api_entity_id)
                            .should_encode(True))
            .auth(Single('Authorization'))
        ).execute()

    def publish_embedded_portal(self,
                                api_entity_id):
        """Does a PUT request to /api-entities/{api_entity_id}/embedded-portal.

        Publish artifacts for an Embedded Portal and get the Portal Embed
        script.
        This endpoint regenerates all the artifacts for an embedded portal and
        uploads them to APIMatic's cloud storage, from where the Portal
        fetches them. These artifacts include:
        1. SDKs
        2. Docs
        3. API Specification files
        Call this endpoint to update your Embedded Portal after you update an
        API Entity via any of the Import API Endpoints. This endpoint returns
        the Portal Embed script in the response.
        __**Note: If you have a hosted portal against the same API Entity,
        artifacts for that portal will get updated as well.**__

        Args:
            api_entity_id (str): The ID of the API Entity to update the portal
                artifacts for.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api-entities/{api_entity_id}/embedded-portal')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('api_entity_id')
                            .value(api_entity_id)
                            .should_encode(True))
            .auth(Single('Authorization'))
        ).execute()

    def generate_on_prem_portal_via_api_entity(self,
                                               api_entity_id):
        """Does a GET request to /api-entities/{api_entity_id}/on-prem-portal.

        Generate an On-premise Documentation Portal for an API Entity. This
        endpoint generates all artifacts for the Portal and packages them
        together into a zip file along with the required HTML, CSS and JS
        files. The generated artifacts include:
        1. SDKs
        2. Docs
        3. API Specification files
        The endpoint returns a zip file that contains a static Site and can be
        hosted on any Web Server.

        Args:
            api_entity_id (str): The ID of the API Entity to generate the
                Portal for.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api-entities/{api_entity_id}/on-prem-portal')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('api_entity_id')
                            .value(api_entity_id)
                            .should_encode(True))
            .auth(Single('Authorization'))
        ).execute()

    def generate_on_prem_portal_via_build_input(self,
                                                file):
        """Does a POST request to /portal.

        Generate an On-premise Documentation Portal by uploading a Portal
        Build Input. This endpoint generates all artifacts for the Portal and
        packages them together into a zip file along with the required HTML,
        CSS and JS files. The generated artifacts include:
        1. SDKs
        2. Docs
        3. API Specification files
        The endpoint returns a zip file that contains a static Site and can be
        hosted on any Web Server.

        Args:
            file (typing.BinaryIO): The input file to the Portal Generator.
                Must contain the build file.

        Returns:
            binary: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream'))
            .auth(Single('Authorization'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'Bad Request', APIException)
            .local_error('401', 'Unauthorized', APIException)
            .local_error('402', 'Subscription Issue', APIException)
            .local_error('422', 'Unprocessable Entity', APIException)
        ).endpoint_configuration(
            EndpointConfiguration()
            .has_binary_response(True)
        ).execute()

    def generate_build_input_for_unpublished_portal(self,
                                                    api_group_id,
                                                    api_entities=None):
        """Does a GET request to /portal/build/{apiGroupId}/draft.

        Generate Build Input for a Portal created using the UI workflow.  The
        Build Input will correspond to the draft version of the Portal i.e.
        unpublished changes will also be included.
        This can be used to create a backup of your Portal or to migrate from
        the UI workflow to the docs as code workflow.

        Args:
            api_group_id (str): TODO: type description here.
            api_entities (List[str], optional): TODO: type description here.

        Returns:
            str: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/build/{apiGroupId}/draft')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('apiGroupId')
                            .value(api_group_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('apiEntities')
                         .value(api_entities))
            .auth(Single('Authorization'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def generate_build_input_for_published_portal(self,
                                                  api_group_id,
                                                  api_entities=None):
        """Does a GET request to /portal/build/{apiGroupId}/published.

        Generate Build Input for a Portal created using the UI workflow.  The
        Build Input will correspond to the published version of the Portal
        i.e. unpublished changes will not be inlcuded.
        This can be used to create a backup of your Portal or to migrate from
        the UI workflow to the docs as code workflow.

        Args:
            api_group_id (str): TODO: type description here.
            api_entities (List[str], optional): TODO: type description here.

        Returns:
            str: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/build/{apiGroupId}/published')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('apiGroupId')
                            .value(api_group_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('apiEntities')
                         .value(api_entities))
            .auth(Single('Authorization'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def unpublish_portal(self,
                         api_entity_id):
        """Does a DELETE request to /api-entities/{api_entity_id}/portal.

        Unpublish a Hosted or Embedded Portal published for an API Entity.
        Calling this endpoint deletes all the published artifacts for a Portal
        from APIMatic's cloud storage. 
        In case of a Hosted Portal, to completely remove the Portal, this
        endpoint needs to be called against all API versions that the Portal
        hosts. 
        In case of an Embedded Portal, to completely remove the Portal, the
        user needs to manually remove the Portal Embed script from the
        embedding site.

        Args:
            api_entity_id (str): The ID of the API Entity to unpublish the
                Portal artifacts for.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api-entities/{api_entity_id}/portal')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('api_entity_id')
                            .value(api_entity_id)
                            .should_encode(True))
            .auth(Single('Authorization'))
        ).execute()

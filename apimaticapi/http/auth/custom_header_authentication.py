# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class CustomHeaderAuthentication(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in CustomHeaderAuthentication

        """
        return "CustomHeaderAuthentication: Authorization is undefined."

    def __init__(self, custom_header_authentication_credentials):
        auth_params = {}
        if custom_header_authentication_credentials is not None \
                and custom_header_authentication_credentials.authorization is not None:
            auth_params["Authorization"] = custom_header_authentication_credentials.authorization
        super().__init__(auth_params=auth_params)


class CustomHeaderAuthenticationCredentials:

    @property
    def authorization(self):
        return self._authorization

    def __init__(self, authorization):
        if authorization is None:
            raise ValueError('authorization cannot be None')
        self._authorization = authorization

    def clone_with(self, authorization=None):
        return CustomHeaderAuthenticationCredentials(
            authorization or self.authorization)

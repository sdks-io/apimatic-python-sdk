# -*- coding: utf-8 -*-

"""
apimaticapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from apimaticapi.configuration import Configuration
from apimaticapi.controllers.base_controller import BaseController
from apimaticapi.configuration import Environment
from apimaticapi.http.auth.custom_header_authentication import CustomHeaderAuthentication
from apimaticapi.controllers.apis_management_controller\
    import ApisManagementController
from apimaticapi.controllers.code_generation_imported_apis_controller\
    import CodeGenerationImportedApisController
from apimaticapi.controllers.code_generation_external_apis_controller\
    import CodeGenerationExternalApisController
from apimaticapi.controllers.transformation_controller\
    import TransformationController
from apimaticapi.controllers.docs_portal_management_controller\
    import DocsPortalManagementController
from apimaticapi.controllers.api_validation_imported_apis_controller\
    import APIValidationImportedApisController
from apimaticapi.controllers.api_validation_external_apis_controller\
    import APIValidationExternalApisController


class ApimaticapiClient(object):
    @LazyProperty
    def apis_management(self):
        return ApisManagementController(self.global_configuration)

    @LazyProperty
    def code_generation_imported_apis(self):
        return CodeGenerationImportedApisController(self.global_configuration)

    @LazyProperty
    def code_generation_external_apis(self):
        return CodeGenerationExternalApisController(self.global_configuration)

    @LazyProperty
    def transformation(self):
        return TransformationController(self.global_configuration)

    @LazyProperty
    def docs_portal_management(self):
        return DocsPortalManagementController(self.global_configuration)

    @LazyProperty
    def api_validation_imported_apis(self):
        return APIValidationImportedApisController(self.global_configuration)

    @LazyProperty
    def api_validation_external_apis(self):
        return APIValidationExternalApisController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, authorization=None,
                 custom_header_authentication_credentials=None, config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, authorization=authorization,
            custom_header_authentication_credentials=custom_header_authentication_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['Authorization']}
        self.auth_managers['Authorization'] = CustomHeaderAuthentication(
            self.config.custom_header_authentication_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)


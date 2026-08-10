
# Getting Started with Apimatic API

## Introduction

This API gives you programmatic access to APIMatic's Code Generation, Docs Generation and Transformation Engine

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install sdksio-apimatic-sdk==3.0.1
```

You can also view the package at:
https://pypi.python.org/pypi/sdksio-apimatic-sdk/3.0.1

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| user_agent | `str` |  |
| custom_url | `str` | The testing domain for the API<br>*Default*: `"https://localhost:44301/api"` |
| environment | [`Environment`](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| custom_header_authentication_credentials | [`CustomHeaderAuthenticationCredentials`](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
import logging

from apimaticapi.apimaticapi_client import ApimaticapiClient
from apimaticapi.configuration import Environment
from apimaticapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from apimaticapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from apimaticapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from apimaticapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration

client = ApimaticapiClient(
    user_agent='user-agent',
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION,
    custom_url='https://localhost:44301/api',
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

### Environment-Based Client Initialization

```python
from apimaticapi.apimaticapi_client import ApimaticapiClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = ApimaticapiClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** |
| TESTING | - |

## Authorization

This API uses the following authentication schemes.

* [`Authorization (Custom Header Signature)`](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/auth/custom-header-signature.md)

## List of APIs

* [Code Generation-External APIs](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/code-generation-external-apis.md)
* [Docs Portal Management](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/docs-portal-management.md)
* [Docs Portal Generation-Async](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/docs-portal-generation-async.md)
* [API Validation-External APIs](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/api-validation-external-apis.md)
* [API Validation V2-External APIs](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/api-validation-v2-external-apis.md)
* [SDK Generation-Async](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/sdk-generation-async.md)
* [Transformation](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/controllers/transformation.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/environment-based-client-initialization.md)
* [AbstractLogger](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/http-request.md)

### Utilities

* [ApiResponse](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/api-response.md)
* [ApiHelper](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/sdks-io/apimatic-python-sdk/tree/3.0.1/doc/unix-date-time.md)


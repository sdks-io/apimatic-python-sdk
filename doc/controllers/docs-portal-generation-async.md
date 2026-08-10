# Docs Portal Generation-Async

```python
docs_portal_generation_async_controller = client.docs_portal_generation_async
```

## Class Name

`DocsPortalGenerationAsyncController`

## Methods

* [Generate on-Prem Portal via Build Input Async](../../doc/controllers/docs-portal-generation-async.md#generate-on-prem-portal-via-build-input-async)
* [Get Portal Generation Status](../../doc/controllers/docs-portal-generation-async.md#get-portal-generation-status)
* [Download Generated Portal](../../doc/controllers/docs-portal-generation-async.md#download-generated-portal)


# Generate on-Prem Portal via Build Input Async

Create an async On-premise Documentation Portal Generation request by providing a Portal Build Input

```python
def generate_on_prem_portal_via_build_input_async(self,
                                                 content_type,
                                                 file,
                                                 x_api_matic_callback_url=None)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `file` | `typing.BinaryIO` | Form, Required | The input file to the Portal Generator. Must contain the build file. |
| `x_api_matic_callback_url` | `str` | Header, Optional | Optional header containing callback url. This url will be called by the server once the portal generation completes |

## Response Type

**202**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PortalGenerationAsyncResponse`](../../doc/models/portal-generation-async-response.md).

## Example Usage

```python
content_type = ContentType.ENUM_MULTIPARTFORMDATA

file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = docs_portal_generation_async_controller.generate_on_prem_portal_via_build_input_async(
    content_type,
    file
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "0194d0da-8d75-7c04-b517-6a9342b114e8",
  "links": {
    "status": "https://api.apimatic.io/portal/v2/0194d0da-8d75-7c04-b517-6a9342b114e8/status",
    "download": "https://api.apimatic.io/portal/v2/0194d0da-8d75-7c04-b517-6a9342b114e8/download"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | [`UnauthorizedResponseException`](../../doc/models/unauthorized-response-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


# Get Portal Generation Status

Get the status of a portal generation request

```python
def get_portal_generation_status(self,
                                id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PortalGenerationStatusResponse`](../../doc/models/portal-generation-status-response.md).

## Example Usage

```python
id = 'id0'

result = docs_portal_generation_async_controller.get_portal_generation_status(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "status": "InProgress"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | [`UnauthorizedResponseException`](../../doc/models/unauthorized-response-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


# Download Generated Portal

Downloads the portal artifacts. The generated artifacts include:

1. SDKs

2. Docs

3. API Specification files

The endpoint returns a zip file that contains a static Site and can be hosted on any Web Server.

```python
def download_generated_portal(self,
                             id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
id = 'id0'

result = docs_portal_generation_async_controller.download_generated_portal(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | [`UnauthorizedResponseException`](../../doc/models/unauthorized-response-exception.md) |
| 422 | Unprocessable Entity - Contains error.zip for build issues | `ApiException` |
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


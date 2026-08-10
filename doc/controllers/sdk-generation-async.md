# SDK Generation-Async

```python
sdk_generation_async_controller = client.sdk_generation_async
```

## Class Name

`SdkGenerationAsyncController`

## Methods

* [Generate SDK via Build Input Async](../../doc/controllers/sdk-generation-async.md#generate-sdk-via-build-input-async)
* [Get SDK Generation Status](../../doc/controllers/sdk-generation-async.md#get-sdk-generation-status)
* [Download Generated SDK](../../doc/controllers/sdk-generation-async.md#download-generated-sdk)


# Generate SDK via Build Input Async

Create an async SDK Generation request by providing a Build Input

```python
def generate_sdk_via_build_input_async(self,
                                      content_type,
                                      file,
                                      language,
                                      x_api_matic_callback_url=None,
                                      package_version=None)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `file` | `typing.BinaryIO` | Form, Required | The input file to the SDK Generator. Must contain the build file or a spec folder containing the API Specification. |
| `language` | [`SdkLanguages`](../../doc/models/sdk-languages.md) | Form, Required | Languages for which SDKs can be generated. |
| `x_api_matic_callback_url` | `str` | Header, Optional | Optional header containing callback url. This url will be called by the server once the SDK generation completes |
| `package_version` | `str` | Form, Optional | Optional field containing the package version to apply to the generated SDK. |

## Response Type

**202**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SdkGenerationAsyncResponse`](../../doc/models/sdk-generation-async-response.md).

## Example Usage

```python
content_type = ContentType.ENUM_MULTIPARTFORMDATA

file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

language = SdkLanguages.CSHARP

package_version = '1.0.0'

result = sdk_generation_async_controller.generate_sdk_via_build_input_async(
    content_type,
    file,
    language,
    package_version=package_version
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
    "status": "https://api.apimatic.io/sdk/0194d0da-8d75-7c04-b517-6a9342b114e8/status",
    "download": "https://api.apimatic.io/sdk/0194d0da-8d75-7c04-b517-6a9342b114e8/download"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | [`UnauthorizedResponseException`](../../doc/models/unauthorized-response-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


# Get SDK Generation Status

Get the status of an SDK generation request

```python
def get_sdk_generation_status(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SdkGenerationStatusResponse`](../../doc/models/sdk-generation-status-response.md).

## Example Usage

```python
id = 'id0'

result = sdk_generation_async_controller.get_sdk_generation_status(id)

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


# Download Generated SDK

Downloads the SDK artifacts. The endpoint returns a zip file containing the generated SDK.

```python
def download_generated_sdk(self,
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

result = sdk_generation_async_controller.download_generated_sdk(id)

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
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


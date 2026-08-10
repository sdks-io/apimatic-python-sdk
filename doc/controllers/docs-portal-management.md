# Docs Portal Management

```python
docs_portal_management_controller = client.docs_portal_management
```

## Class Name

`DocsPortalManagementController`


# Generate on-Prem Portal via Build Input

Generate an On-premise Documentation Portal by uploading a Portal Build Input. This endpoint generates all artifacts for the Portal and packages them together into a zip file along with the required HTML, CSS and JS files. The generated artifacts include:

1. SDKs
2. Docs
3. API Specification files

The endpoint returns a zip file that contains a static Site and can be hosted on any Web Server.

```python
def generate_on_prem_portal_via_build_input(self,
                                           content_type,
                                           file,
                                           _optional_query_parameters=None)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `file` | `typing.BinaryIO` | Form, Required | The input file to the Portal Generator. Must contain the build file. |
| `_optional_query_parameters` | `array` | Optional | Pass additional query parameters. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
content_type = ContentType.ENUM_MULTIPARTFORMDATA

file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

_optional_query_parameters = {
    'key0': 'additionalQueryParams2'
}

result = docs_portal_management_controller.generate_on_prem_portal_via_build_input(
    content_type,
    file,
    _optional_query_parameters=_optional_query_parameters
)

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
| 403 | Subscription Issue | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 422 | Unprocessable Entity - Contains error.zip for build issues | `ApiException` |
| 500 | Internal Server Error | [`InternalServerErrorResponseException`](../../doc/models/internal-server-error-response-exception.md) |


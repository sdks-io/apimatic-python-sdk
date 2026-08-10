# Code Generation-External APIs

```python
code_generation_external_apis_controller = client.code_generation_external_apis
```

## Class Name

`CodeGenerationExternalApisController`

## Methods

* [Generate SDK via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file)
* [Generate SDK via URL](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url)
* [Download SDK](../../doc/controllers/code-generation-external-apis.md#download-sdk)
* [List All Code Generations](../../doc/controllers/code-generation-external-apis.md#list-all-code-generations)
* [Download Input File](../../doc/controllers/code-generation-external-apis.md#download-input-file)
* [Get a Code Generation](../../doc/controllers/code-generation-external-apis.md#get-a-code-generation)
* [Delete Code Generation for External APIs](../../doc/controllers/code-generation-external-apis.md#delete-code-generation-for-external-apis)


# Generate SDK via File

Generate an SDK for an API by by uploading the API specification file.

This endpoint generates and then uploads the generated SDK to APIMatic's cloud storage. An ID for the generation performed is returned as part of the response.

This endpoint does not import an API into APIMatic.

```python
def generate_sdk_via_file(self,
                         accept,
                         file,
                         template,
                         _optional_query_parameters=None)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | [`Accept`](../../doc/models/accept.md) | Header, Required | Must be set to 'application/json' to ensure JSON response format |
| `file` | `typing.BinaryIO` | Form, Required | The API specification file.<br>The type of the specification file should be any of the [supported formats](https://docs.apimatic.io/api-transformer/overview-transformer#supported-input-formats). |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Form, Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in. |
| `_optional_query_parameters` | `array` | Optional | Pass additional query parameters. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserCodeGeneration`](../../doc/models/user-code-generation.md).

## Example Usage

```python
accept = Accept.ENUM_APPLICATIONJSON

file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

template = Platforms.CS_NET_STANDARD_LIB

_optional_query_parameters = {
    'key0': 'additionalQueryParams2'
}

result = code_generation_external_apis_controller.generate_sdk_via_file(
    accept,
    file,
    template,
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
| 400 | Bad Request | [`BadRequestResponseSdkException`](../../doc/models/bad-request-response-sdk-exception.md) |
| 401 | Unauthorized | [`UnauthorizedResponseException`](../../doc/models/unauthorized-response-exception.md) |
| 403 | Subscription Issue | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Generate SDK via URL

Generate an SDK for an API by providing the URL of the API specification file.

This endpoint generates and then uploads the generated SDK to APIMatic's cloud storage. An ID for the generation performed is returned as part of the response.

This endpoint does not import an API into APIMatic.

```python
def generate_sdk_via_url(self,
                        body)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GenerateSdkViaUrlRequest`](../../doc/models/generate-sdk-via-url-request.md) | Body, Required | Request Body |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserCodeGeneration`](../../doc/models/user-code-generation.md).

## Example Usage

```python
body = GenerateSdkViaUrlRequest(
    url='http://petstore.swagger.io/v2/swagger.json',
    template=Platforms.CS_NET_STANDARD_LIB
)

result = code_generation_external_apis_controller.generate_sdk_via_url(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Download SDK

Download the SDK generated via the Generate SDK endpoints.

```python
def download_sdk(self,
                codegen_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of code generation received in the response of the [Generate SDK Via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file) or [Generate SDK Via URL ](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.download_sdk(codegen_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List All Code Generations

Get a list of all SDK generations performed with external APIs via the Generate SDK endpoints.

```python
def list_all_code_generations(self)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[UserCodeGeneration]`](../../doc/models/user-code-generation.md).

## Example Usage

```python
result = code_generation_external_apis_controller.list_all_code_generations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Download Input File

Download the API Specification file used as input for a specific SDK generation performed via the Generate SDK endpoints.

```python
def download_input_file(self,
                       codegen_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to download the API specification for. The code generation ID is received in the response of the [Generate SDK Via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file) or [Generate SDK Via URL ](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url) calls |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.download_input_file(codegen_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get a Code Generation

Get details on an SDK generation performed for an external API via the Generate SDK endpoints.

```python
def get_a_code_generation(self,
                         codegen_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to fetch. The code generation ID is received in the response of the [Generate SDK Via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file) or [Generate SDK Via URL ](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserCodeGeneration`](../../doc/models/user-code-generation.md).

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.get_a_code_generation(codegen_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Code Generation for External APIs

Delete an SDK generation performed for an API via the Generate SDK endpoints.

```python
def delete_code_generation_for_external_apis(self,
                                            codegen_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to delete. The code generation ID is received in the response of the [Generate SDK Via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file) or [Generate SDK Via URL ](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.delete_code_generation_for_external_apis(codegen_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


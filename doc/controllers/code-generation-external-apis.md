# Code Generation-External APIs

```python
code_generation_external_apis_controller = client.code_generation_external_apis
```

## Class Name

`CodeGenerationExternalApisController`

## Methods

* [Generate SDK Via File](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-file)
* [Generate SDK Via URL](../../doc/controllers/code-generation-external-apis.md#generate-sdk-via-url)
* [Download Generated SDK](../../doc/controllers/code-generation-external-apis.md#download-generated-sdk)
* [List All Code Generations External](../../doc/controllers/code-generation-external-apis.md#list-all-code-generations-external)
* [Download Input File Codegen](../../doc/controllers/code-generation-external-apis.md#download-input-file-codegen)
* [Get a Code Generation Codegen](../../doc/controllers/code-generation-external-apis.md#get-a-code-generation-codegen)
* [Delete Code Generation 1](../../doc/controllers/code-generation-external-apis.md#delete-code-generation-1)


# Generate SDK Via File

Generate an SDK for an API by by uploading the API specification file.

This endpoint generates and then uploads the generated SDK to APIMatic's cloud storage. An ID for the generation performed is returned as part of the response.

This endpoint does not import an API into APIMatic.

```python
def generate_sdk_via_file(self,
                         file,
                         template)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | The API specification file.<br>The type of the specification file should be any of the [supported formats](https://docs.apimatic.io/api-transformer/overview-transformer#supported-input-formats). |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Form, Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in. |

## Response Type

[`UserCodeGeneration`](../../doc/models/user-code-generation.md)

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

template = Platforms.CS_NET_STANDARD_LIB

result = code_generation_external_apis_controller.generate_sdk_via_file(
    file,
    template
)
print(result)
```


# Generate SDK Via URL

Generate an SDK for an API by providing the URL of the API specification file.

This endpoint generates and then uploads the generated SDK to APIMatic's cloud storage. An ID for the generation performed is returned as part of the response.

This endpoint does not import an API into APIMatic.

```python
def generate_sdk_via_url(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GenerateSdkViaUrlRequest`](../../doc/models/generate-sdk-via-url-request.md) | Body, Required | Request Body |

## Response Type

[`UserCodeGeneration`](../../doc/models/user-code-generation.md)

## Example Usage

```python
body = GenerateSdkViaUrlRequest(
    url='http://petstore.swagger.io/v2/swagger.json',
    template=Platforms.CS_NET_STANDARD_LIB
)

result = code_generation_external_apis_controller.generate_sdk_via_url(body)
print(result)
```


# Download Generated SDK

Download the SDK generated via the Generate SDK endpoints.

```python
def download_generated_sdk(self,
                          codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of code generation received in the response of the [Generate SDK Via File](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-file) or [Generate SDK Via URL ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-url) calls. |

## Response Type

`binary`

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.download_generated_sdk(codegen_id)
print(result)
```


# List All Code Generations External

Get a list of all SDK generations performed with external APIs via the Generate SDK endpoints.

```python
def list_all_code_generations_external(self)
```

## Response Type

[`List[UserCodeGeneration]`](../../doc/models/user-code-generation.md)

## Example Usage

```python
result = code_generation_external_apis_controller.list_all_code_generations_external()
print(result)
```


# Download Input File Codegen

Download the API Specification file used as input for a specific SDK generation performed via the Generate SDK endpoints.

```python
def download_input_file_codegen(self,
                               codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to download the API specification for. The code generation ID is received in the response of the [Generate SDK Via File](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-file) or [Generate SDK Via URL ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-url) calls |

## Response Type

`binary`

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.download_input_file_codegen(codegen_id)
print(result)
```


# Get a Code Generation Codegen

Get details on an SDK generation performed for an external API via the Generate SDK endpoints.

```python
def get_a_code_generation_codegen(self,
                                 codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to fetch. The code generation ID is received in the response of the [Generate SDK Via File](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-file) or [Generate SDK Via URL ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-url) calls. |

## Response Type

[`UserCodeGeneration`](../../doc/models/user-code-generation.md)

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.get_a_code_generation_codegen(codegen_id)
print(result)
```


# Delete Code Generation 1

Delete an SDK generation performed for an API via the Generate SDK endpoints.

```python
def delete_code_generation_1(self,
                            codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to delete. The code generation ID is received in the response of the [Generate SDK Via File](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-file) or [Generate SDK Via URL ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-external-apis/generate-sdk-via-url) calls. |

## Response Type

`void`

## Example Usage

```python
codegen_id = 'codegen_id6'

result = code_generation_external_apis_controller.delete_code_generation_1(codegen_id)
print(result)
```


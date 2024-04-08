# Code Generation-Imported APIs

```python
code_generation_imported_apis_controller = client.code_generation_imported_apis
```

## Class Name

`CodeGenerationImportedApisController`

## Methods

* [Generate SDK](../../doc/controllers/code-generation-imported-apis.md#generate-sdk)
* [Download SDK](../../doc/controllers/code-generation-imported-apis.md#download-sdk)
* [List All Code Generations Imported](../../doc/controllers/code-generation-imported-apis.md#list-all-code-generations-imported)
* [Get a Code Generation Imported](../../doc/controllers/code-generation-imported-apis.md#get-a-code-generation-imported)
* [Delete Code Generation](../../doc/controllers/code-generation-imported-apis.md#delete-code-generation)


# Generate SDK

Generate an SDK for an API Version.

This endpoint generates and then uploads the generated SDK to APIMatic's cloud storage. An ID for the generation performed is returned as part of the response.

```python
def generate_sdk(self,
                api_entity_id,
                template)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_entity_id` | `str` | Template, Required | The ID of the API Entity to generate the SDK for. |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Form, Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in. |

## Response Type

[`APIEntityCodeGeneration`](../../doc/models/api-entity-code-generation.md)

## Example Usage

```python
api_entity_id = 'api_entity_id4'

template = Platforms.CS_NET_STANDARD_LIB

result = code_generation_imported_apis_controller.generate_sdk(
    api_entity_id,
    template
)
print(result)
```


# Download SDK

Download the SDK generated via the Generate SDK endpoint.

```python
def download_sdk(self,
                api_entity_id,
                codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_entity_id` | `str` | Template, Required | The ID of the API Entity for which the SDK was generated. |
| `codegen_id` | `str` | Template, Required | The ID of code generation received in the response of the [SDK generation call](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-imported-apis/generate-sdk). |

## Response Type

`binary`

## Example Usage

```python
api_entity_id = 'api_entity_id4'

codegen_id = 'codegen_id6'

result = code_generation_imported_apis_controller.download_sdk(
    api_entity_id,
    codegen_id
)
print(result)
```


# List All Code Generations Imported

Get a list of all SDK generations done against an API Version via the Generate SDK endpoint.

```python
def list_all_code_generations_imported(self,
                                      api_entity_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_entity_id` | `str` | Template, Required | The ID of the API Entity for which to list code generations. |

## Response Type

[`List[APIEntityCodeGeneration]`](../../doc/models/api-entity-code-generation.md)

## Example Usage

```python
api_entity_id = 'api_entity_id4'

result = code_generation_imported_apis_controller.list_all_code_generations_imported(api_entity_id)
print(result)
```


# Get a Code Generation Imported

Get details on an SDK generation performed via the Generate SDK endpoint.

```python
def get_a_code_generation_imported(self,
                                  api_entity_id,
                                  codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_entity_id` | `str` | Template, Required | The ID of the API Entity to fetch the code generation for. |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to fetch. The code generation ID is received in the response of the [SDK generation call](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-imported-apis/generate-sdk). |

## Response Type

[`APIEntityCodeGeneration`](../../doc/models/api-entity-code-generation.md)

## Example Usage

```python
api_entity_id = 'api_entity_id4'

codegen_id = 'codegen_id6'

result = code_generation_imported_apis_controller.get_a_code_generation_imported(
    api_entity_id,
    codegen_id
)
print(result)
```


# Delete Code Generation

Delete an SDK generation performed for an API Version via the Generate SDK endpoint.

```python
def delete_code_generation(self,
                          api_entity_id,
                          codegen_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_entity_id` | `str` | Template, Required | The ID of the API Entity to delete the code generation for. |
| `codegen_id` | `str` | Template, Required | The ID of the code generation to delete. The code generation ID is received in the response of the [SDK generation call](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/code-generation-imported-apis/generate-sdk). |

## Response Type

`void`

## Example Usage

```python
api_entity_id = 'api_entity_id4'

codegen_id = 'codegen_id6'

result = code_generation_imported_apis_controller.delete_code_generation(
    api_entity_id,
    codegen_id
)
print(result)
```


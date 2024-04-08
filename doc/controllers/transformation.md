# Transformation

```python
transformation_controller = client.transformation
```

## Class Name

`TransformationController`

## Methods

* [Transform Via File](../../doc/controllers/transformation.md#transform-via-file)
* [Transform Via URL](../../doc/controllers/transformation.md#transform-via-url)
* [Download Transformed File](../../doc/controllers/transformation.md#download-transformed-file)
* [Download Input File Transformation](../../doc/controllers/transformation.md#download-input-file-transformation)
* [List All Transformations](../../doc/controllers/transformation.md#list-all-transformations)
* [Get a Transformation](../../doc/controllers/transformation.md#get-a-transformation)
* [Delete Transformation](../../doc/controllers/transformation.md#delete-transformation)


# Transform Via File

Transform an API into any of the supported API specification formats by uploading the API specification file. This endpoint transforms and then uploads the transformed API specification to APIMatic's cloud storage. An ID for the transformation performed is returned as part of the response.

```python
def transform_via_file(self,
                      file,
                      export_format)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | The API specification file.<br>The type of the specification file should be any of the [supported formats](https://docs.apimatic.io/api-transformer/overview-transformer#supported-input-formats). |
| `export_format` | [`ExportFormats`](../../doc/models/export-formats.md) | Form, Required | The structure contains API specification formats that Transformer can convert to. |

## Response Type

[`Transformation`](../../doc/models/transformation.md)

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

export_format = ExportFormats.WSDL

result = transformation_controller.transform_via_file(
    file,
    export_format
)
print(result)
```


# Transform Via URL

Transform an API into any of the supported API specification formats by providing the URL of the API specification file.

This endpoint transforms and then uploads the transformed API specification to APIMatic's cloud storage. An ID for the transformation performed is returned as part of the response.

```python
def transform_via_url(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransformViaUrlRequest`](../../doc/models/transform-via-url-request.md) | Body, Required | Request Body |

## Response Type

[`Transformation`](../../doc/models/transformation.md)

## Example Usage

```python
body = TransformViaUrlRequest(
    url='https://petstore.swagger.io/v2/swagger.json',
    export_format=ExportFormats.APIMATIC
)

result = transformation_controller.transform_via_url(body)
print(result)
```


# Download Transformed File

Download the transformed API specification file transformed via the Transformation endpoints.

```python
def download_transformed_file(self,
                             transformation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of transformation received in the response of the [Transform Via File ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-file) or [Transform Via URL  ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-url) calls. |

## Response Type

`binary`

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.download_transformed_file(transformation_id)
print(result)
```


# Download Input File Transformation

Download the API Specification file used as input for a particular Transformation performed via the Transformation endpoints.

```python
def download_input_file_transformation(self,
                                      transformation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to download the API specification for. The transformation ID is received in the response of the [Transform Via File ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-file) or [Transform Via URL](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-url) calls. |

## Response Type

`binary`

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.download_input_file_transformation(transformation_id)
print(result)
```


# List All Transformations

Get a list of all API transformations performed.

```python
def list_all_transformations(self)
```

## Response Type

[`List[Transformation]`](../../doc/models/transformation.md)

## Example Usage

```python
result = transformation_controller.list_all_transformations()
print(result)
```


# Get a Transformation

Get details on a particular Transformation performed via the Transformation endpoints.

```python
def get_a_transformation(self,
                        transformation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to fetch. The transformation ID is received in the response of the [Transform Via File ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-file) or [Transform Via URL  ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-url) calls. |

## Response Type

[`Transformation`](../../doc/models/transformation.md)

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.get_a_transformation(transformation_id)
print(result)
```


# Delete Transformation

Delete a particular Transformation performed for an API via the Transformation endpoints.

```python
def delete_transformation(self,
                         transformation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to delete. The transformation ID is received in the response of the [Transform Via File ](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-file) or [Transform Via URL](https://www.apimatic.io/api-docs-preview/dashboard/60eea3b7a73395c3052d961b/v/3_0#/http/api-endpoints/transformation/transform-via-url) calls. |

## Response Type

`void`

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.delete_transformation(transformation_id)
print(result)
```


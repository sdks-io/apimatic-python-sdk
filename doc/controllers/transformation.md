# Transformation

```python
transformation_controller = client.transformation
```

## Class Name

`TransformationController`

## Methods

* [Transform via File](../../doc/controllers/transformation.md#transform-via-file)
* [Transform via URL](../../doc/controllers/transformation.md#transform-via-url)
* [Download Transformed File](../../doc/controllers/transformation.md#download-transformed-file)
* [Download Input File](../../doc/controllers/transformation.md#download-input-file)
* [List All Transformations](../../doc/controllers/transformation.md#list-all-transformations)
* [Get a Transformation](../../doc/controllers/transformation.md#get-a-transformation)
* [Delete Transformation](../../doc/controllers/transformation.md#delete-transformation)


# Transform via File

Transform an API into any of the supported API specification formats by uploading the API specification file.

This endpoint transforms and then uploads the transformed API specification to APIMatic's cloud storage. An ID for the transformation performed is returned as part of the response.

```python
def transform_via_file(self,
                      content_type,
                      file,
                      export_format,
                      _optional_query_parameters=None)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `file` | `typing.BinaryIO` | Form, Required | The API specification file.<br>The type of the specification file should be any of the [supported formats](https://docs.apimatic.io/api-transformer/overview-transformer#supported-input-formats). |
| `export_format` | [`ExportFormats`](../../doc/models/export-formats.md) | Form, Required | The structure contains API specification formats that Transformer can convert to. |
| `_optional_query_parameters` | `array` | Optional | Pass additional query parameters. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Transformation`](../../doc/models/transformation.md).

## Example Usage

```python
content_type = ContentType.ENUM_MULTIPARTFORMDATA

file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

export_format = ExportFormats.WSDL

_optional_query_parameters = {
    'key0': 'additionalQueryParams2'
}

result = transformation_controller.transform_via_file(
    content_type,
    file,
    export_format,
    _optional_query_parameters=_optional_query_parameters
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Transform via URL

Transform an API into any of the supported API specification formats by providing the URL of the API specification file.

This endpoint transforms and then uploads the transformed API specification to APIMatic's cloud storage. An ID for the transformation performed is returned as part of the response.

```python
def transform_via_url(self,
                     body)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransformViaUrlRequest`](../../doc/models/transform-via-url-request.md) | Body, Required | Request Body |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Transformation`](../../doc/models/transformation.md).

## Example Usage

```python
body = TransformViaUrlRequest(
    url='https://petstore.swagger.io/v2/swagger.json',
    export_format=ExportFormats.APIMATIC
)

result = transformation_controller.transform_via_url(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Download Transformed File

Download the transformed API specification file transformed via the Transformation endpoints.

```python
def download_transformed_file(self,
                             transformation_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of transformation received in the response of the [Transform Via File ](../../doc/controllers/transformation.md#transform-via-file) or [Transform Via URL  ](../../doc/controllers/transformation.md#transform-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.download_transformed_file(transformation_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Download Input File

Download the API Specification file used as input for a particular Transformation performed via the Transformation endpoints.

```python
def download_input_file(self,
                       transformation_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to download the API specification for. The transformation ID is received in the response of the [Transform Via File ](../../doc/controllers/transformation.md#transform-via-file) or [Transform Via URL](../../doc/controllers/transformation.md#transform-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.download_input_file(transformation_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List All Transformations

Get a list of all API transformations performed.

```python
def list_all_transformations(self)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Transformation]`](../../doc/models/transformation.md).

## Example Usage

```python
result = transformation_controller.list_all_transformations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get a Transformation

Get details on a particular Transformation performed via the Transformation endpoints.

```python
def get_a_transformation(self,
                        transformation_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to fetch. The transformation ID is received in the response of the [Transform Via File ](../../doc/controllers/transformation.md#transform-via-file) or [Transform Via URL  ](../../doc/controllers/transformation.md#transform-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Transformation`](../../doc/models/transformation.md).

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.get_a_transformation(transformation_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Transformation

Delete a particular Transformation performed for an API via the Transformation endpoints.

```python
def delete_transformation(self,
                         transformation_id)
```

## Authentication

This endpoint requires [Authorization](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformation_id` | `str` | Template, Required | The ID of the transformation to delete. The transformation ID is received in the response of the [Transform Via File ](../../doc/controllers/transformation.md#transform-via-file) or [Transform Via URL](../../doc/controllers/transformation.md#transform-via-url) calls. |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
transformation_id = 'transformation_id6'

result = transformation_controller.delete_transformation(transformation_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


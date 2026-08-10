
# Transform via Url Request

This structure puts together the URL of the file to be transformed, along with the desired export format.

*This model accepts additional fields of type Any.*

## Structure

`TransformViaUrlRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | The URL for the API specification file.<br><br>**Note:** This URL should be publicly accessible. |
| `export_format` | [`ExportFormats`](../../doc/models/export-formats.md) | Required | The structure contains API specification formats that Transformer can convert to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.export_formats import ExportFormats
from apimaticapi.models.transform_via_url_request import TransformViaUrlRequest

transform_via_url_request = TransformViaUrlRequest(
    url='https://petstore.swagger.io/v2/swagger.json',
    export_format=ExportFormats.APIMATIC,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


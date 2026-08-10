
# Generate Sdk via Url Request

*This model accepts additional fields of type Any.*

## Structure

`GenerateSdkViaUrlRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | The URL for the API specification file.<br><br>**Note:** This URL should be publicly accessible. |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in.<br><br>**Default**: `"CS_NET_STANDARD_LIB"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.generate_sdk_via_url_request import GenerateSdkViaUrlRequest
from apimaticapi.models.platforms import Platforms

generate_sdk_via_url_request = GenerateSdkViaUrlRequest(
    url='http://petstore.swagger.io/v2/swagger.json',
    template=Platforms.CS_NET_STANDARD_LIB,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


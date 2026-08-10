
# Sdk Generation Status Response

## Structure

`SdkGenerationStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status`](../../doc/models/status.md) | Required | - |
| `errors` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.sdk_generation_status_response import SdkGenerationStatusResponse
from apimaticapi.models.status import Status

sdk_generation_status_response = SdkGenerationStatusResponse(
    status=Status.INPROGRESS,
    errors={
        'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


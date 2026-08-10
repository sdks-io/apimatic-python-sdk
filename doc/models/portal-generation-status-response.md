
# Portal Generation Status Response

## Structure

`PortalGenerationStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status`](../../doc/models/status.md) | Required | - |
| `errors` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.portal_generation_status_response import PortalGenerationStatusResponse
from apimaticapi.models.status import Status

portal_generation_status_response = PortalGenerationStatusResponse(
    status=Status.INPROGRESS,
    errors={
        'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        'key1': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


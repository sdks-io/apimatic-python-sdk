
# Sdk Generation Async Response

## Structure

`SdkGenerationAsyncResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | - |
| `links` | [`Links`](../../doc/models/links.md) | Required | - |

## Example

```python
import jsonpickle

from apimaticapi.models.links import Links
from apimaticapi.models.sdk_generation_async_response import SdkGenerationAsyncResponse

sdk_generation_async_response = SdkGenerationAsyncResponse(
    id='0194d0da-8d75-7c04-b517-6a9342b114e8',
    links=Links(
        status='https://api.apimatic.io/sdk/0194d0da-8d75-7c04-b517-6a9342b114e8/status',
        download='https://api.apimatic.io/sdk/0194d0da-8d75-7c04-b517-6a9342b114e8/download',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    )
)
```


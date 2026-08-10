
# Bad Request Response Sdk Exception

Standard JSON error response for bad requests

*This model accepts additional fields of type Any.*

## Structure

`BadRequestResponseSdkException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | Error message describing the bad request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except BadRequestResponseSdkException as e:
    print(e)
except ApiException as e:
    print(e)
```


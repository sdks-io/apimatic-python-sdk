
# Problem Details Exception

*This model accepts additional fields of type Any.*

## Structure

`ProblemDetailsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `status` | `int` | Optional | - |
| `detail` | `str` | Optional | - |
| `instance` | `str` | Optional | - |
| `errors` | `Dict[str, Any]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ProblemDetailsException as e:
    print(e)
except ApiException as e:
    print(e)
```



# Line Info

*This model accepts additional fields of type Any.*

## Structure

`LineInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_line_number` | `int` | Required | - |
| `start_line_position` | `int` | Required | - |
| `end_line_number` | `int` | Required | - |
| `end_line_position` | `int` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.line_info import LineInfo

line_info = LineInfo(
    start_line_number=10,
    start_line_position=146,
    end_line_number=10,
    end_line_position=178,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


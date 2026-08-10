
# Validation Entry

*This model accepts additional fields of type Any.*

## Structure

`ValidationEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | - |
| `line_info` | [`LineInfo`](../../doc/models/line-info.md) | Optional | - |
| `json_reference_path` | `str` | Optional | - |
| `file_reference` | `str` | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `rule_documentation_reference` | `str` | Optional | - |
| `additional_references` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.line_info import LineInfo
from apimaticapi.models.validation_entry import ValidationEntry

validation_entry = ValidationEntry(
    message='message0',
    line_info=LineInfo(
        start_line_number=162,
        start_line_position=6,
        end_line_number=142,
        end_line_position=74,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    json_reference_path='jsonReferencePath6',
    file_reference='fileReference8',
    metadata={
        'key0': 'metadata7'
    },
    rule_documentation_reference='ruleDocumentationReference0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


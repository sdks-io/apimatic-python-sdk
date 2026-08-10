
# Validation Summary

*This model accepts additional fields of type Any.*

## Structure

`ValidationSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_success` | `bool` | Required | - |
| `blocking` | [`List[ValidationEntry]`](../../doc/models/validation-entry.md) | Required | - |
| `errors` | [`List[ValidationEntry]`](../../doc/models/validation-entry.md) | Required | - |
| `warnings` | [`List[ValidationEntry]`](../../doc/models/validation-entry.md) | Required | - |
| `information` | [`List[ValidationEntry]`](../../doc/models/validation-entry.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.line_info import LineInfo
from apimaticapi.models.validation_entry import ValidationEntry
from apimaticapi.models.validation_summary import ValidationSummary

validation_summary = ValidationSummary(
    is_success=False,
    blocking=[
        ValidationEntry(
            message='message4',
            line_info=LineInfo(
                start_line_number=162,
                start_line_position=6,
                end_line_number=142,
                end_line_position=74,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            json_reference_path='jsonReferencePath0',
            file_reference='fileReference2',
            metadata={
                'key0': 'metadata9',
                'key1': 'metadata0',
                'key2': 'metadata1'
            },
            rule_documentation_reference='ruleDocumentationReference4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    errors=[
        ValidationEntry(
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
                'key0': 'metadata3'
            },
            rule_documentation_reference='ruleDocumentationReference0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    warnings=[
        ValidationEntry(
            message='message4',
            line_info=LineInfo(
                start_line_number=162,
                start_line_position=6,
                end_line_number=142,
                end_line_position=74,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            json_reference_path='jsonReferencePath0',
            file_reference='fileReference2',
            metadata={
                'key0': 'metadata1',
                'key1': 'metadata0',
                'key2': 'metadata9'
            },
            rule_documentation_reference='ruleDocumentationReference4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    information=[
        ValidationEntry(
            message='message4',
            line_info=LineInfo(
                start_line_number=162,
                start_line_position=6,
                end_line_number=142,
                end_line_position=74,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            json_reference_path='jsonReferencePath0',
            file_reference='fileReference2',
            metadata={
                'key0': 'metadata9'
            },
            rule_documentation_reference='ruleDocumentationReference4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


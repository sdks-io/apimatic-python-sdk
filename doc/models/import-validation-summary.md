
# Import Validation Summary

## Structure

`ImportValidationSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Required | - |
| `errors` | `List[str]` | Required | - |
| `warnings` | `List[str]` | Required | - |
| `messages` | `List[str]` | Required | - |

## Example (as JSON)

```json
{
  "success": true,
  "errors": [],
  "warnings": [],
  "messages": [
    "One or more elements in the API specification has a missing description field."
  ]
}
```



# Field

This structure encapsulates all details of a parameter.

## Structure

`Field`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `optional` | `bool` | Required | If parameter is optional |
| `mtype` | `str` | Required | Type of Parameter |
| `constant` | `bool` | Required | IF Parameter is constant |
| `is_array` | `bool` | Required | If Param is collected as array |
| `is_stream` | `bool` | Required | - |
| `is_attribute` | `bool` | Required | - |
| `is_map` | `bool` | Required | - |
| `attributes` | [`Attributes`](../../doc/models/attributes.md) | Required | The structure contain attribute details of a parameter type. |
| `nullable` | `bool` | Required | If Parameter is nullable |
| `id` | `str` | Required | Unique Parameter identifier |
| `name` | `str` | Required | Parameter Name |
| `description` | `str` | Required | Parameter Description |
| `default_value` | `str` | Required | Default Values of a Parameter |

## Example (as JSON)

```json
{
  "optional": false,
  "type": "test\\r\\nstringEncoding",
  "constant": false,
  "isArray": false,
  "isStream": false,
  "isAttribute": false,
  "isMap": false,
  "attributes": {
    "id": "5be1603083b41d0b50110551"
  },
  "nullable": false,
  "id": "5a4e8675b724bb198c289f7a",
  "name": "body",
  "description": "description4",
  "defaultValue": "defaultValue0"
}
```



# Authentication

This Structure encapsulates all details of API authentication.

## Structure

`Authentication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Auth Id |
| `auth_type` | `str` | Required | Auth Type |
| `scopes` | [`List[AuthScope]`](../../doc/models/auth-scope.md) | Required | Scope |
| `parameters` | `List[str]` | Required | Auth Params |
| `auth_scopes` | `List[str]` | Required | Auth Scopes |
| `auth_grant_types` | `List[str]` | Required | Auth Grant Types |
| `param_formats` | `object` | Required | Paramater Formats |

## Example (as JSON)

```json
{
  "id": "5be0a21a83b41d0d8cdcd80f",
  "authType": "None",
  "scopes": [],
  "parameters": [],
  "authScopes": [],
  "authGrantTypes": [],
  "paramFormats": {}
}
```



# Generate SDK Via File Request Body

## Structure

`GenerateSDKViaFileRequestBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `binary` | Required | The API specification file.<br>The type of the specification file should be any of the [supported formats](https://docs.apimatic.io/api-transformer/overview-transformer#supported-input-formats). |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in.<br>**Default**: `'CS_NET_STANDARD_LIB'` |

## Example (as JSON)

```json
{
  "file": "file4",
  "template": "CS_NET_STANDARD_LIB"
}
```


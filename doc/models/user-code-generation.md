
# User Code Generation

The Code Generation structure encapsulates all the  the details of an SDK generation performed by a user.

## Structure

`UserCodeGeneration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique Code Generation Identifier |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in.<br>**Default**: `'CS_NET_STANDARD_LIB'` |
| `generated_file` | `str` | Required | The generated SDK |
| `generated_on` | `datetime` | Required | Generation Date and Time |
| `hash_code` | `str` | Required | The md5 hash of the API Description |
| `code_generation_source` | `str` | Required | Generation Source |
| `code_gen_version` | `str` | Required | Generation Version |
| `success` | `bool` | Required | Generation Status |
| `user_id` | `str` | Required | Unique User Identifier |
| `input_file` | `str` | Required | API Specification file in a supported format |

## Example (as JSON)

```json
{
  "id": "5be08b2d83b41d0d8cdb3289",
  "template": "CS_NET_STANDARD_LIB",
  "generatedFile": "https://api.apimatic.io/code-generations/5be08b2d83b41d0d8cdb3289/generated-sdk",
  "generatedOn": "04/03/2024 15:46:32",
  "hashCode": "77BDA4F625EF512B336D0A77CE2BB2B6",
  "codeGenerationSource": "Api",
  "codeGenVersion": "1",
  "success": true,
  "userId": "5afc60380b9949253c6b7776",
  "inputFile": "https://api.apimatic.io/code-generations/5be08d7b83b41d0d8cdb3958/input-file"
}
```


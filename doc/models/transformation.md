
# Transformation

Transformation structure encapsulates all the details of a Transformation.

## Structure

`Transformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique Transformation Identifier |
| `transformed_on` | `str` | Required | Transformation Date and Time |
| `user_id` | `str` | Required | Unique User Identifier |
| `inputted_file` | `str` | Required | API Specification file to be transformed |
| `generated_file` | `str` | Required | API Specification file transformed to desired format |
| `export_format` | `str` | Required | Desired Specification format |
| `transformation_source` | `str` | Required | Source of Transformation |
| `transformation_input` | `str` | Required | Via File or URL |
| `code_gen_version` | `str` | Required | CodeGen Engine Version |
| `success` | `bool` | Required | Successful Transformation Flag |
| `import_summary` | [`ApiValidationSummary`](../../doc/models/api-validation-summary.md) | Required | - |
| `api_validation_summary` | [`ApiValidationSummary`](../../doc/models/api-validation-summary.md) | Required | - |

## Example (as JSON)

```json
{
  "id": "5be0999183b41d0d8cdb9f26",
  "transformedOn": "2018-11-05T19:27:13.2062198Z",
  "userId": "5afc60380b9949253c6b7776",
  "inputtedFile": "https://api.apimatic.io/transformations/5be0999183b41d0d8cdb9f26/input-file",
  "generatedFile": "https://api.apimatic.io/transformations/5be0999183b41d0d8cdb9f26/converted-file",
  "exportFormat": "APIMATIC",
  "transformationSource": "ViaApi",
  "transformationInput": "File",
  "codeGenVersion": "1",
  "importSummary": {
    "success": true,
    "errors": [],
    "warnings": [],
    "messages": [
      "Input identified as <i><code>OpenAPI v3.0 (YAML)</code></i>.",
      "A test case generated from example values for endpoint <i><code>RecentTransactionsNew</code></i> in group <i><code>Transaction</code></i>."
    ]
  },
  "apiValidationSummary": {
    "success": true,
    "errors": [],
    "warnings": [
      "The example specified contains undeclared fields.  (<a href=\"https://docs.apimatic.io/rulesets/apimatic-docs-linting/no-undeclared-fields-in-example-value\" target=\"_blank\" rel=\"nofollow\">View Details</a>)<br/><b>Source</b>: <i><code>API > Endpoints > Invoice[4] > searchstatementofaccount [POST, /invoice-management/v1/searchstatementofaccount] > Default Response > Examples[0] > Example Value</code></i>. <br/><b>Undeclared Fields</b>: <i><code>Data</code></i><br/><b>Component Name/Identifier</b>: <i><code>response</code></i>. "
    ],
    "messages": [
      "One or more elements in the API specification has a missing description.  (<a href=\"https://docs.apimatic.io/rulesets/apimatic-docs-linting/required-description-all-entities\" target=\"_blank\" rel=\"nofollow\">View Details</a>)<br/><b>Source</b>: <i><code>API</code></i>. "
    ]
  },
  "success": true
}
```


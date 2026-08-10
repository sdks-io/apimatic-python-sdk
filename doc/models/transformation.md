
# Transformation

Transformation structure encapsulates all the details of a Transformation.

*This model accepts additional fields of type Any.*

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from apimaticapi.models.api_validation_summary import ApiValidationSummary
from apimaticapi.models.transformation import Transformation

transformation = Transformation(
    id='5be0999183b41d0d8cdb9f26',
    transformed_on='11/5/2018 7:27:13 PM',
    user_id='5afc60380b9949253c6b7776',
    inputted_file='https://api.apimatic.io/transformations/5be0999183b41d0d8cdb9f26/input-file',
    generated_file='https://api.apimatic.io/transformations/5be0999183b41d0d8cdb9f26/converted-file',
    export_format='APIMATIC',
    transformation_source='Api',
    transformation_input='File',
    code_gen_version='1',
    success=True,
    import_summary=ApiValidationSummary(
        success=True,
        errors=[],
        warnings=[
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getRealTimeData</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getRealTimeData</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDataPerCategory</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDataPerCategory</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getData</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getData</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveStatuses</code></i> of group <i><code>statuses</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveStatuses</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>200</code></i> in endpoint <i><code>getDevices</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>deviceModelId</code></i>, <i><code>manufacturer</code></i>, <i><code>model</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDevices</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDevices</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getAlarms</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getAlarms</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveAlerts</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveAlerts</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getAlerts</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getAlerts</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getConfiguration</code></i> of group <i><code>configuration data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getConfiguration</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveAlarms</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveAlarms</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getPowerCurves</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getPowerCurves</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDataSignals</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDataSignals</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getStatuses</code></i> of group <i><code>statuses</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getStatuses</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getSites</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getSites</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.'
        ],
        messages=[
            'One or more elements in the API specification has a missing description field.'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    api_validation_summary=ApiValidationSummary(
        success=True,
        errors=[],
        warnings=[
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getRealTimeData</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getRealTimeData</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDataPerCategory</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDataPerCategory</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getData</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getData</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveStatuses</code></i> of group <i><code>statuses</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveStatuses</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>200</code></i> in endpoint <i><code>getDevices</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>deviceModelId</code></i>, <i><code>manufacturer</code></i>, <i><code>model</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDevices</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDevices</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getAlarms</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getAlarms</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveAlerts</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveAlerts</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getAlerts</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getAlerts</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getConfiguration</code></i> of group <i><code>configuration data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getConfiguration</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getActiveAlarms</code></i> of group <i><code>alerts</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getActiveAlarms</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getPowerCurves</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getPowerCurves</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getDataSignals</code></i> of group <i><code>data</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getDataSignals</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getStatuses</code></i> of group <i><code>statuses</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getStatuses</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.',
            'Media type <i><code>application/json; charset=utf-8</code></i> content definition of response code <i><code>429</code></i> in endpoint <i><code>getSites</code></i> of group <i><code>assets</code></i> contains an example value with following undeclared fields: <i><code>detail</i></code>.',
            'Endpoint <i><code>getSites</code></i> has an example specified for error code <i><code>429</code></i> which contains following undeclared fields: <i><code>detail</i></code>.'
        ],
        messages=[
            'One or more elements in the API specification has a missing description field.'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


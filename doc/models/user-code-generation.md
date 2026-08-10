
# User Code Generation

The Code Generation structure encapsulates all the  the details of an SDK generation performed by a user.

*This model accepts additional fields of type Any.*

## Structure

`UserCodeGeneration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique Code Generation Identifier |
| `template` | [`Platforms`](../../doc/models/platforms.md) | Required | The structure contains platforms that APIMatic CodeGen can generate SDKs and Docs in.<br><br>**Default**: `"CS_NET_STANDARD_LIB"` |
| `generated_file` | `str` | Required | The generated SDK |
| `generated_on` | `datetime` | Required | Generation Date and Time |
| `hash_code` | `str` | Required | The md5 hash of the API Description |
| `code_generation_source` | `str` | Required | Generation Source |
| `code_gen_version` | `str` | Required | Generation Version |
| `success` | `bool` | Required | Generation Status |
| `user_id` | `str` | Required | Unique User Identifier |
| `input_file` | `str` | Required | API Specification file in a supported format |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from apimaticapi.models.platforms import Platforms
from apimaticapi.models.user_code_generation import UserCodeGeneration

user_code_generation = UserCodeGeneration(
    id='5be08b2d83b41d0d8cdb3289',
    template=Platforms.CS_NET_STANDARD_LIB,
    generated_file='https://api.apimatic.io/code-generations/5be08b2d83b41d0d8cdb3289/generated-sdk',
    generated_on=dateutil.parser.parse('2018-11-05T18:25:46Z'),
    hash_code='77BDA4F625EF512B336D0A77CE2BB2B6',
    code_generation_source='Api',
    code_gen_version='1',
    success=True,
    user_id='5afc60380b9949253c6b7776',
    input_file='https://api.apimatic.io/code-generations/5be08d7b83b41d0d8cdb3958/input-file',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```


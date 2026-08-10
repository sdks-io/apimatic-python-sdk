
# Custom Header Signature



Documentation for accessing and setting credentials for Authorization.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Authorization | `str` | Auth Header. Replace {x-auth-key} with your Auth Key. | `authorization` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from apimaticapi.apimaticapi_client import ApimaticapiClient
from apimaticapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = ApimaticapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    )
)
```



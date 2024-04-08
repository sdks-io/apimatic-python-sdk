
# Code Gen Settings

APIMatic’s code generation engine has various code generation configurations to customise the behaviour and outlook across the generated SDKS. This structure encapsulates all settings for CodeGeneration.

## Structure

`CodeGenSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_async` | `bool` | Required | Generate asynchronous code for API Calls and deserialization |
| `use_http_method_prefix` | `bool` | Required | Use HTTP Method prefixes for endpoint wrappers |
| `use_model_prefix` | `bool` | Required | Use "Model" postfixes for generated class names |
| `use_enum_prefix` | `bool` | Required | Use "Enum" postfixes for enumerated types |
| `use_constructors_for_config` | `bool` | Required | - |
| `use_common_sdk_library` | `bool` | Required | Use common SDK library to reduce code duplication |
| `generate_interfaces` | `bool` | Required | Generates interfaces for controller classes in the generated SDKs |
| `generate_appveyor_config` | `bool` | Required | Generate Appveyor configuration file |
| `generate_circle_config` | `bool` | Required | Generate CircleCI configuration file |
| `generate_jenkins_config` | `bool` | Required | Generate Jenkins configuration file |
| `generate_travis_config` | `bool` | Required | Generate Travis CI configuration file |
| `android_use_app_manifest` | `bool` | Required | Use "AndroidManifest.xml" for config variables in Android |
| `ios_use_app_info_plist` | `bool` | Required | Use "App-Info.plist" file for config variables in iOS |
| `ios_generate_core_data` | `bool` | Required | Generate "CoreData" schema and entity classes in iOS? |
| `runscope_enabled` | `bool` | Required | Enable runscope |
| `collapse_params_to_array` | `bool` | Required | Collect Parameters as arrays |
| `preserve_parameter_order` | `bool` | Required | Attempts to preserve parameter order for endpoints |
| `append_content_headers` | `bool` | Required | Append JSON/XML accept and content-type headers |
| `model_serialization_is_json` | `bool` | Required | - |
| `nullify_404` | `bool` | Required | Return a null value on HTTP 404 |
| `validate_required_parameters` | `bool` | Required | Validate required parameters to be Not Null |
| `enable_additional_model_properties` | `bool` | Required | Allow models to have additional runtime properties |
| `java_use_properties_config` | `bool` | Required | - |
| `use_controller_prefix` | `bool` | Required | Use "Controller" postfixes for generated controller classes |
| `use_exception_prefix` | `bool` | Required | Use Exception Prefixes |
| `parameter_array_format` | `str` | Required | Parameter Array format with index or without |
| `obj_c_http_client` | `str` | Required | Configure the HTTP client for Objective C |
| `c_sharp_http_client` | `str` | Required | Configure the HTTP client for C# |
| `android_http_client` | `str` | Required | Configure the HTTP client for  Android |
| `node_http_client` | `str` | Required | Configure the HTTP client for node |
| `php_http_client` | `str` | Required | Configure the HTTP client for PHP |
| `body_serialization` | `int` | Required | - |
| `array_serialization` | `str` | Required | Specify type of array serialisation |
| `timeout` | `int` | Required | This option specifies the duration (in seconds) after which requests would timeout |
| `enable_logging` | `bool` | Required | Enabling this generates code in the SDKs for logging events in the API cycle using a library. |
| `enable_http_cache` | `bool` | Required | Enabling caching of responses (not available in all languages) |
| `retries` | `int` | Required | Specify number of retries |
| `retry_interval` | `int` | Required | Specify retry interval in case of failures |
| `generate_advanced_docs` | `bool` | Required | Generate advanced read me files |
| `store_timezone_information` | `bool` | Required | Store Timezone information for the generation |
| `enable_php_composer_version_string` | `bool` | Required | Use "Controller" postfixes for generated controller classes |
| `security_protocols` | `List[str]` | Required | Specify Security Protocols |
| `underscore_numbers` | `bool` | Required | Use underscores before and after numbers for underscore case |
| `use_singleton_pattern` | `bool` | Required | Allow usage of a Singleton Pattern |
| `disable_linting` | `bool` | Required | Files/dependencies used for linting are not generated if this option is enabled |
| `allow_skipping_ssl_cert_verification` | `bool` | Required | Create a configuration option in SDKs to optionally skip certificate verification when establishing HTTPS connections. |
| `apply_customizations` | `List[str]` | Required | Apply Customisations |
| `do_not_split_words` | `List[str]` | Required | Enabling this will stop splitting of words when converting identifiers from API specification to language-specific identifiers. |
| `sort_resources` | `bool` | Required | Sorts resources such as endpoints, endpoint groups and models in generated documentation |
| `enable_global_user_agent` | `bool` | Required | Enable a global user agent |

## Example (as JSON)

```json
{
  "isAsync": true,
  "useHttpMethodPrefix": true,
  "useModelPrefix": false,
  "useEnumPrefix": true,
  "useConstructorsForConfig": false,
  "useCommonSdkLibrary": false,
  "generateInterfaces": false,
  "generateAppveyorConfig": false,
  "generateCircleConfig": false,
  "generateJenkinsConfig": false,
  "generateTravisConfig": false,
  "androidUseAppManifest": false,
  "iosUseAppInfoPlist": false,
  "iosGenerateCoreData": false,
  "runscopeEnabled": false,
  "collapseParamsToArray": false,
  "preserveParameterOrder": true,
  "appendContentHeaders": true,
  "modelSerializationIsJSON": true,
  "nullify404": false,
  "validateRequiredParameters": false,
  "enableAdditionalModelProperties": false,
  "javaUsePropertiesConfig": false,
  "useControllerPrefix": true,
  "useExceptionPrefix": true,
  "parameterArrayFormat": "ParamArrayWithIndex",
  "objCHttpClient": "UNIREST",
  "cSharpHttpClient": "UNIREST",
  "androidHttpClient": "ANDROID_OK",
  "nodeHttpClient": "NODE_REQUEST",
  "phpHttpClient": "UNIREST",
  "bodySerialization": 0,
  "arraySerialization": "Indexed",
  "timeout": 0,
  "enableLogging": false,
  "enableHttpCache": false,
  "retries": 0,
  "retryInterval": 1,
  "generateAdvancedDocs": true,
  "storeTimezoneInformation": false,
  "enablePhpComposerVersionString": false,
  "securityProtocols": [
    "Ssl3",
    "Tls"
  ],
  "underscoreNumbers": true,
  "useSingletonPattern": true,
  "disableLinting": false,
  "allowSkippingSSLCertVerification": false,
  "applyCustomizations": [],
  "doNotSplitWords": [],
  "sortResources": false,
  "enableGlobalUserAgent": true
}
```


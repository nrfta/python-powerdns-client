# powerdns_client.DefaultApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error**](DefaultApi.md#error) | **GET** /error | Will always generate an error

# **error**
> error()

Will always generate an error

### Example
```python
from __future__ import print_function
import time
import powerdns_client
from powerdns_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = powerdns_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = powerdns_client.DefaultApi(powerdns_client.ApiClient(configuration))

try:
    # Will always generate an error
    api_instance.error()
except ApiException as e:
    print("Exception when calling DefaultApi->error: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


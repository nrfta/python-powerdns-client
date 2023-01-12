# powerdns_client.StatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.

# **get_stats**
> get_stats(server_id, statistic=statistic, includerings=includerings)

Query statistics.

Query PowerDNS internal statistics.

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
api_instance = powerdns_client.StatsApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
statistic = 'statistic_example' # str | When set to the name of a specific statistic, only this value is returned. If no statistic with that name exists, the response has a 422 status and an error message.  (optional)
includerings = true # bool | “true” (default) or “false”, whether to include the Ring items, which can contain thousands of log messages or queried domains. Setting this to ”false” may make the response a lot smaller. (optional) (default to true)

try:
    # Query statistics.
    api_instance.get_stats(server_id, statistic=statistic, includerings=includerings)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **statistic** | **str**| When set to the name of a specific statistic, only this value is returned. If no statistic with that name exists, the response has a 422 status and an error message.  | [optional] 
 **includerings** | **bool**| “true” (default) or “false”, whether to include the Ring items, which can contain thousands of log messages or queried domains. Setting this to ”false” may make the response a lot smaller. | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


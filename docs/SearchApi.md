# powerdns_client.SearchApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_data**](SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS


# **search_data**
> SearchResults search_data(server_id, q, max, object_type=object_type)

Search the data inside PowerDNS

Search the data inside PowerDNS for search_term and return at most max_results. This includes zones, records and comments. The * character can be used in search_term as a wildcard character and the ? character can be used as a wildcard for a single character.

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
api_instance = powerdns_client.SearchApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
q = 'q_example' # str | The string to search for
max = 56 # int | Maximum number of entries to return
object_type = 'object_type_example' # str | Type of data to search for, one of “all”, “zone”, “record”, “comment” (optional)

try:
    # Search the data inside PowerDNS
    api_response = api_instance.search_data(server_id, q, max, object_type=object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **q** | **str**| The string to search for | 
 **max** | **int**| Maximum number of entries to return | 
 **object_type** | **str**| Type of data to search for, one of “all”, “zone”, “record”, “comment” | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


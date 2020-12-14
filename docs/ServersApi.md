# powerdns_client.ServersApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cache_flush_by_name**](ServersApi.md#cache_flush_by_name) | **PUT** /servers/{server_id}/cache/flush | Flush a cache-entry by name
[**list_server**](ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
[**list_servers**](ServersApi.md#list_servers) | **GET** /servers | List all servers


# **cache_flush_by_name**
> CacheFlushResult cache_flush_by_name(server_id, domain)

Flush a cache-entry by name

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
api_instance = powerdns_client.ServersApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
domain = 'domain_example' # str | The domain name to flush from the cache

try:
    # Flush a cache-entry by name
    api_response = api_instance.cache_flush_by_name(server_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServersApi->cache_flush_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **domain** | **str**| The domain name to flush from the cache | 

### Return type

[**CacheFlushResult**](CacheFlushResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_server**
> Server list_server(server_id)

List a server

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
api_instance = powerdns_client.ServersApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve

try:
    # List a server
    api_response = api_instance.list_server(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServersApi->list_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**Server**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_servers**
> list[Server] list_servers()

List all servers

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
api_instance = powerdns_client.ServersApi(powerdns_client.ApiClient(configuration))

try:
    # List all servers
    api_response = api_instance.list_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServersApi->list_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Server]**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# powerdns_client.AutoprimaryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_autoprimary**](AutoprimaryApi.md#create_autoprimary) | **POST** /servers/{server_id}/autoprimaries | Add an autoprimary
[**delete_autoprimary**](AutoprimaryApi.md#delete_autoprimary) | **DELETE** /servers/{server_id}/autoprimaries/{ip}/{nameserver} | Delete the autoprimary entry
[**get_autoprimaries**](AutoprimaryApi.md#get_autoprimaries) | **GET** /servers/{server_id}/autoprimaries | Get a list of autoprimaries

# **create_autoprimary**
> create_autoprimary(autoprimary, server_id)

Add an autoprimary

This methods add a new autoprimary server.

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
api_instance = powerdns_client.AutoprimaryApi(powerdns_client.ApiClient(configuration))
autoprimary = powerdns_client.Autoprimary() # Autoprimary | autoprimary entry to add
server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on

try:
    # Add an autoprimary
    api_instance.create_autoprimary(autoprimary, server_id)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->create_autoprimary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoprimary** | [**Autoprimary**](Autoprimary.md)| autoprimary entry to add | 
 **server_id** | **str**| The id of the server to manage the list of autoprimaries on | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_autoprimary**
> delete_autoprimary(server_id, ip, nameserver)

Delete the autoprimary entry

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
api_instance = powerdns_client.AutoprimaryApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to delete the autoprimary from
ip = 'ip_example' # str | IP address of autoprimary
nameserver = 'nameserver_example' # str | DNS name of the autoprimary

try:
    # Delete the autoprimary entry
    api_instance.delete_autoprimary(server_id, ip, nameserver)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->delete_autoprimary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to delete the autoprimary from | 
 **ip** | **str**| IP address of autoprimary | 
 **nameserver** | **str**| DNS name of the autoprimary | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autoprimaries**
> Autoprimary get_autoprimaries(server_id)

Get a list of autoprimaries

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
api_instance = powerdns_client.AutoprimaryApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on

try:
    # Get a list of autoprimaries
    api_response = api_instance.get_autoprimaries(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoprimaryApi->get_autoprimaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to manage the list of autoprimaries on | 

### Return type

[**Autoprimary**](Autoprimary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


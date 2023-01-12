# powerdns_client.ZonemetadataApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata**](ZonemetadataApi.md#create_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
[**delete_metadata**](ZonemetadataApi.md#delete_metadata) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
[**get_metadata**](ZonemetadataApi.md#get_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a Metadata object.
[**list_metadata**](ZonemetadataApi.md#list_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the Metadata associated with the zone.
[**modify_metadata**](ZonemetadataApi.md#modify_metadata) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Replace the content of a single kind of domain metadata.

# **create_metadata**
> create_metadata(metadata, server_id, zone_id)

Creates a set of metadata entries

Creates a set of metadata entries of given kind for the zone. Existing metadata entries for the zone with the same kind are not overwritten.

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
api_instance = powerdns_client.ZonemetadataApi(powerdns_client.ApiClient(configuration))
metadata = powerdns_client.Metadata() # Metadata | Metadata object with list of values to create
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 

try:
    # Creates a set of metadata entries
    api_instance.create_metadata(metadata, server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->create_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**Metadata**](Metadata.md)| Metadata object with list of values to create | 
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata**
> delete_metadata(server_id, zone_id, metadata_kind)

Delete all items of a single kind of domain metadata.

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
api_instance = powerdns_client.ZonemetadataApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
metadata_kind = 'metadata_kind_example' # str | The kind of metadata

try:
    # Delete all items of a single kind of domain metadata.
    api_instance.delete_metadata(server_id, zone_id, metadata_kind)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->delete_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| The kind of metadata | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> Metadata get_metadata(server_id, zone_id, metadata_kind)

Get the content of a single kind of domain metadata as a Metadata object.

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
api_instance = powerdns_client.ZonemetadataApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
metadata_kind = 'metadata_kind_example' # str | The kind of metadata

try:
    # Get the content of a single kind of domain metadata as a Metadata object.
    api_response = api_instance.get_metadata(server_id, zone_id, metadata_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| The kind of metadata | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata**
> list[Metadata] list_metadata(server_id, zone_id)

Get all the Metadata associated with the zone.

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
api_instance = powerdns_client.ZonemetadataApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Get all the Metadata associated with the zone.
    api_response = api_instance.list_metadata(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->list_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_metadata**
> Metadata modify_metadata(metadata, server_id, zone_id, metadata_kind)

Replace the content of a single kind of domain metadata.

Creates a set of metadata entries of given kind for the zone. Existing metadata entries for the zone with the same kind are removed.

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
api_instance = powerdns_client.ZonemetadataApi(powerdns_client.ApiClient(configuration))
metadata = powerdns_client.Metadata() # Metadata | metadata to add/create
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
metadata_kind = 'metadata_kind_example' # str | The kind of metadata

try:
    # Replace the content of a single kind of domain metadata.
    api_response = api_instance.modify_metadata(metadata, server_id, zone_id, metadata_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->modify_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**Metadata**](Metadata.md)| metadata to add/create | 
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata_kind** | **str**| The kind of metadata | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


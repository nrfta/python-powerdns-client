# powerdns_client.ZonesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**axfr_export_zone**](ZonesApi.md#axfr_export_zone) | **GET** /servers/{server_id}/zones/{zone_id}/export | Returns the zone in AXFR format.
[**axfr_retrieve_zone**](ZonesApi.md#axfr_retrieve_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/axfr-retrieve | Retrieve slave zone from its master.
[**create_zone**](ZonesApi.md#create_zone) | **POST** /servers/{server_id}/zones | Creates a new domain, returns the Zone on creation.
[**delete_zone**](ZonesApi.md#delete_zone) | **DELETE** /servers/{server_id}/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
[**list_zone**](ZonesApi.md#list_zone) | **GET** /servers/{server_id}/zones/{zone_id} | zone managed by a server
[**list_zones**](ZonesApi.md#list_zones) | **GET** /servers/{server_id}/zones | List all Zones in a server
[**notify_zone**](ZonesApi.md#notify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/notify | Send a DNS NOTIFY to all slaves.
[**patch_zone**](ZonesApi.md#patch_zone) | **PATCH** /servers/{server_id}/zones/{zone_id} | Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
[**put_zone**](ZonesApi.md#put_zone) | **PUT** /servers/{server_id}/zones/{zone_id} | Modifies basic zone data.
[**rectify_zone**](ZonesApi.md#rectify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/rectify | Rectify the zone data.

# **axfr_export_zone**
> InlineResponse200 axfr_export_zone(server_id, zone_id)

Returns the zone in AXFR format.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Returns the zone in AXFR format.
    api_response = api_instance.axfr_export_zone(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->axfr_export_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **axfr_retrieve_zone**
> axfr_retrieve_zone(server_id, zone_id)

Retrieve slave zone from its master.

Fails when zone kind is not Slave, or slave is disabled in the configuration. Clients MUST NOT send a body.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Retrieve slave zone from its master.
    api_instance.axfr_retrieve_zone(server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->axfr_retrieve_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_zone**
> Zone create_zone(zone_struct, server_id, rrsets=rrsets)

Creates a new domain, returns the Zone on creation.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
zone_struct = powerdns_client.Zone() # Zone | The zone struct to patch with
server_id = 'server_id_example' # str | The id of the server to retrieve
rrsets = true # bool | “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. (optional) (default to true)

try:
    # Creates a new domain, returns the Zone on creation.
    api_response = api_instance.create_zone(zone_struct, server_id, rrsets=rrsets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->create_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 
 **server_id** | **str**| The id of the server to retrieve | 
 **rrsets** | **bool**| “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. | [optional] [default to true]

### Return type

[**Zone**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(server_id, zone_id)

Deletes this zone, all attached metadata and rrsets.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Deletes this zone, all attached metadata and rrsets.
    api_instance.delete_zone(server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->delete_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone**
> Zone list_zone(server_id, zone_id, rrsets=rrsets, rrset_name=rrset_name, rrset_type=rrset_type)

zone managed by a server

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
rrsets = true # bool | “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. (optional) (default to true)
rrset_name = 'rrset_name_example' # str | Limit output to RRsets for this name. (optional)
rrset_type = 'rrset_type_example' # str | Limit output to the RRset of this type. Can only be used together with rrset_name. (optional)

try:
    # zone managed by a server
    api_response = api_instance.list_zone(server_id, zone_id, rrsets=rrsets, rrset_name=rrset_name, rrset_type=rrset_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->list_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **rrsets** | **bool**| “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. | [optional] [default to true]
 **rrset_name** | **str**| Limit output to RRsets for this name. | [optional] 
 **rrset_type** | **str**| Limit output to the RRset of this type. Can only be used together with rrset_name. | [optional] 

### Return type

[**Zone**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zones**
> list[Zone] list_zones(server_id, zone=zone, dnssec=dnssec)

List all Zones in a server

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone = 'zone_example' # str | When set to the name of a zone, only this zone is returned. If no zone with that name exists, the response is an empty array. This can e.g. be used to check if a zone exists in the database without having to guess/encode the zone's id or to check if a zone exists.  (optional)
dnssec = true # bool | “true” (default) or “false”, whether to include the “dnssec” and ”edited_serial” fields in the Zone objects. Setting this to ”false” will make the query a lot faster. (optional) (default to true)

try:
    # List all Zones in a server
    api_response = api_instance.list_zones(server_id, zone=zone, dnssec=dnssec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->list_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone** | **str**| When set to the name of a zone, only this zone is returned. If no zone with that name exists, the response is an empty array. This can e.g. be used to check if a zone exists in the database without having to guess/encode the zone&#x27;s id or to check if a zone exists.  | [optional] 
 **dnssec** | **bool**| “true” (default) or “false”, whether to include the “dnssec” and ”edited_serial” fields in the Zone objects. Setting this to ”false” will make the query a lot faster. | [optional] [default to true]

### Return type

[**list[Zone]**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_zone**
> notify_zone(server_id, zone_id)

Send a DNS NOTIFY to all slaves.

Fails when zone kind is not Master or Slave, or master and slave are disabled in the configuration. Only works for Slave if renotify is on. Clients MUST NOT send a body.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Send a DNS NOTIFY to all slaves.
    api_instance.notify_zone(server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->notify_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_zone**
> patch_zone(zone_struct, server_id, zone_id)

Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
zone_struct = powerdns_client.Zone() # Zone | The zone struct to patch with
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 

try:
    # Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
    api_instance.patch_zone(zone_struct, server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->patch_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 
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

# **put_zone**
> put_zone(zone_struct, server_id, zone_id)

Modifies basic zone data.

The only fields in the zone structure which can be modified are: kind, masters, catalog, account, soa_edit, soa_edit_api, api_rectify, dnssec, and nsec3param. All other fields are ignored.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
zone_struct = powerdns_client.Zone() # Zone | The zone struct to patch with
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 

try:
    # Modifies basic zone data.
    api_instance.put_zone(zone_struct, server_id, zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->put_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 
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

# **rectify_zone**
> str rectify_zone(server_id, zone_id)

Rectify the zone data.

This does not take into account the API-RECTIFY metadata. Fails on slave zones and zones that do not have DNSSEC.

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
api_instance = powerdns_client.ZonesApi(powerdns_client.ApiClient(configuration))
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try:
    # Rectify the zone data.
    api_response = api_instance.rectify_zone(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->rectify_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# TSIGKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the key | [optional] 
**id** | **str** | The ID for this key, used in the TSIGkey URL endpoint. | [optional] 
**algorithm** | **str** | The algorithm of the TSIG key | [optional] 
**key** | **str** | The Base64 encoded secret key, empty when listing keys. MAY be empty when POSTing to have the server generate the key material | [optional] 
**type** | **str** | Set to \&quot;TSIGKey\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# Cryptokey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | set to \&quot;Cryptokey\&quot; | [optional] 
**id** | **int** | The internal identifier, read only | [optional] 
**keytype** | **str** |  | [optional] 
**active** | **bool** | Whether or not the key is in active use | [optional] 
**published** | **bool** | Whether or not the DNSKEY record is published in the zone | [optional] 
**dnskey** | **str** | The DNSKEY record for this key | [optional] 
**ds** | **list[str]** | An array of DS records for this key | [optional] 
**cds** | **list[str]** | An array of DS records for this key, filtered by CDS publication settings | [optional] 
**privatekey** | **str** | The private key in ISC format | [optional] 
**algorithm** | **str** | The name of the algorithm of the key, should be a mnemonic | [optional] 
**bits** | **int** | The size of the key | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


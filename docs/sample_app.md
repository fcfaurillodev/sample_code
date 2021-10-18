
# Sample App



## Indices

* [Merchant API](#merchant-api)

  * [Create Merchant](#1-create-merchant)
  * [Delete Merchant](#2-delete-merchant)
  * [Get Merchant](#3-get-merchant)
  * [Get Merchants](#4-get-merchants)
  * [Update Merchant](#5-update-merchant)

* [Ungrouped](#ungrouped)

  * [Healtcheck](#1-healtcheck)


--------


## Merchant API



### 1. Create Merchant



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{base_url}}/api/merchant
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| client-id | {{app_client_id}} |  |
| Authorization | Bearer {{token}} |  |
| Content-Type | application/json |  |



***Body:***

```js        
{
    "merchant_name": "Sample Merchant",
    "identity_id": "123456",
    "description": "sample description",
    "contact_number": "092000000",
    "contact_email": "sample@mail.com",
    "contact_person": "sample name",
    "address": "sample address"
}
```



### 2. Delete Merchant



***Endpoint:***

```bash
Method: DELETE
Type: RAW
URL: {{base_url}}/api/merchant/10
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| client-id | {{app_client_id}} |  |
| Authorization | Bearer {{token}} |  |
| Content-Type | application/json |  |



### 3. Get Merchant



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{base_url}}/api/merchant/{{merchant_id}}
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| client-id | {{app_client_id}} |  |
| Authorization | Bearer {{token}} |  |
| Content-Type | application/json |  |



### 4. Get Merchants



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{base_url}}/api/merchants
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| client-id | {{app_client_id}} |  |
| Authorization | Bearer {{token}} |  |
| Content-Type | application/json |  |



***Query params:***

| Key | Value | Description |
| --- | ------|-------------|
| page | 1 |  |
| limit | 100 |  |



### 5. Update Merchant



***Endpoint:***

```bash
Method: PATCH
Type: RAW
URL: {{base_url}}/api/merchant/10
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| client-id | {{app_client_id}} |  |
| Authorization | Bearer {{token}} |  |
| Content-Type | application/json |  |



***Body:***

```js        
{
    "merchant_name": "Test Merchant"
}
```



## Ungrouped



### 1. Healtcheck



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{base_url}}/api/healthcheck
```



---
[Back to top](#sample-app)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2021-10-17 12:55:37 by [docgen](https://github.com/thedevsaddam/docgen)

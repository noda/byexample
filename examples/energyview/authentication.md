# EnergyView API: Authentication

[Back to index](/index.html)

This example shows how to authenticate to the EnergyView APIv1.

The API uses keys to authenticate requests. An API key is a unique string of characters that is used to identify the calling system and provide it with access to the resources.

To view and manage API keys, you need to have administrative access to the account page.

> API keys carry important privileges and should be kept secure at all times. It is important not to share your secret API keys in publicly accessible areas such as social media, client-side code, and so forth.

Authentication to the API is performed using HTTP Key Auth. This means that you need to provide your API key as the auth key value in the request header. You do not need to provide a password. For example, the Authorization header should be set as follows:

> *Authorization: Key secret-token.c4bbcb1fbec99d65…9afa73bd4e39a8a*

It is important to note that all API requests must be made over HTTPS. API requests that are not authenticated using the API key will fail.

```python
import requests

domain = "mydomain"
secret = "mysecretkey"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/nodes"

reply = requests.get(url, headers=header)

if reply.status_code == 200:
    print("Request succeeded")
else:
    print("Request failed")
```
```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    domain := "mydomain"
    secret := "mysecretkey"
    url := fmt.Sprintf("https://customer.noda.se/%s/api/v1/nodes", domain)

    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        panic(err)
    }

    req.Header.Set("Authorization", fmt.Sprintf("Key %s", secret))

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("Response status:", resp.Status)
}
```
```javascript
const https = require('https');

const domain = 'mydomain';
const secret = 'mysecretkey';
const url = `https://customer.noda.se/${domain}/api/v1/nodes`;
const headers = {
  Authorization: `Key ${secret}`,
};

https.get(url, { headers }, (res) => {
  if (res.statusCode === 200) {
    console.log('Request succeeded');
  } else {
    console.log('Request failed');
  }
}).on('error', (error) => {
  console.error(error);
});
```

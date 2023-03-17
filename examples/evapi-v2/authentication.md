# Authentication

[Back to index](/index.html)

This example shows how to authenticate to the EnergyView APIv2.

The API uses keys to authenticate requests. An API key is a unique string of characters that is used to identify the calling system and provide it with access to the resources.

To view and manage API keys, you need to have administrative access to the account page.

> API keys carry important privileges and should be kept secure at all times. It is important not to share your secret API keys in publicly accessible areas such as social media, client-side code, and so forth.

Authentication to the API is performed using HTTP Basic Auth. The username is the domain name and the password is the API key. For example, the Authorization header should be set as follows:

> *Authorization: Basic aDR4WDByOnNvMTMzN3VS*

For details about HTTP Basic Auth, see [RFC 7617](https://tools.ietf.org/html/rfc7617). Or if you want, you can read Wikipedia's [article](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side).

It is important to note that all API requests must be made over HTTPS. API requests that are not authenticated using the API key will fail.

```python
import requests

domain = "mydomain"
secret = "mysecretkey"
url = f"https://customer.noda.se/api/v2/nodes"

reply = requests.get(url, auth=(domain, secret))

if reply.status_code == 200:
    print("Request succeeded")
else:
    print("Request failed")
```

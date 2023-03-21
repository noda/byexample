---
priority: 20
---
# Create a Building Node

[Back to index](/index.html)


This guide demonstrates how to create a Building Node using the EnergyView API v1.

For more information about the API, refer to the online [API documentation](https://customer.noda.se/api/v1).

## A Basic Use Case

Let's say we want to create a Building Node for a building with the address "251 North Bristol Avenue". The building is a residential building with 5 apartments. We want to monitor the temperature in each apartment and control the heating system. The temperature sensors are already added to the system and now we want to add the Node which represents the buildings heating system.

To create this Node, send a POST request to the `/{domain}/api/v1/nodes` endpoint.

The entities we need to have are:

- A device type (Kelp-Basic is the most common for legacy reasons). The device type determines the available sensors we can bind to our Node.
- Name (address or similar).
- The type of building, commercial or residential.
- An optional description of the Node.
- The position of the Building (latitude, longitude).

Here is an example of how to create a Building Node:

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"http://canary.lvh.me/{domain}/api/v1/nodes"

body = {
  "name": "251 North Bristol Avenue",
  "designation": "building/residential",
  "description": "My Control Node for my building",
  "tags": [
    "outdoortemp",
    "outdoortemp_fake",
    "outdoortemp_offset",
    "returntemp_sec",
    "supplytemp_sec",
    "supplytemp_sec_controller_setvalue",
    "supplytemp_sec_offset",
  ],
  "device": "Kelp-Basic",
  "state": "in-use"
}

response = requests.post(url, json=body, headers=header)
print(response.json())  # {'uuid': '67abd0a0-6c2c-4d7c-9d4b-7c4f4b4b1e9a', 'id': 123}
```
```json
{
  "uuid": "67abd0a0-6c2c-4d7c-9d4b-7c4f4b4b1e9a",
  "name": "251 North Bristol Avenue",
  "designation": "building/residential",
  "description": "string",
  "tags": [
    "outdoortemp",
    "outdoortemp_fake",
    "outdoortemp_offset",
    "returntemp_sec",
    "supplytemp_sec",
    "supplytemp_sec_controller_setvalue",
    "supplytemp_sec_offset",
  
  ],
  "device": "Kelp-Basic",
  "state": "in-use"
}
```

The Node is now created and we can begin storing data for the tags we specified. See the [Write TimeSeries data](write-timeseries-data.html) guide for more information.


## Setting the location

The location of the Building Node can be set by doing a `POST` requests to the metadata endpoint `/{domain}/api/v1/nodes/{node_id}/metadata`.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
node_id = 1931
url = f"http://canary.lvh.me/{domain}/api/v1/nodes/{node_id}/metadata"

body = [
    {"key": "lat", "value": "29.9792"},
    {"key": "lon", "value": "31.1344"},
]

params = {"overwrite": "true"}  # Overwrite any existing values

reply = requests.post(url, json=body, headers=header, params=params)
if reply.status_code == 204:
    print("Success")
else:
    print("Error")
```

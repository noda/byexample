---
priority: 21
---
# Create an Indoor Sensor Node

[Back to index](/index.html)

This guide will show you how to create a Node that represents an indoor sensor.

For more information about the API, refer to the online [API documentation](https://customer.noda.se/api/v1).

## A Basic Use Case

To add a Node that represents an indoor sensor, send a POST request to the `/{domain}/api/v1/nodes` endpoint.

The entities we need to have are:

- Name (address or similar).
- The parent Node (the Building Node).
- An optional description of the Node.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"http://canary.lvh.me/{domain}/api/v1/nodes"

parent_node_id = 1931
body = {
  "name": "251 North Bristol Avenue, Apartment 1",
  "designation": "sensor/indoor",
  "description": "Apartment 1",
  "tags": [
    "indoortemp",
    "humidity",
  ],
  "parent": parent_node_id,
  "device": "Generic Indoor Sensor",
  "state": "in-use"
}

reply = requests.post(url, json=body, headers=header)
if reply.status_code == 201:
    # Set the position of the Node
    node_id = reply.json()["uuid"]
    url = f"http://canary.lvh.me/{domain}/api/v1/nodes/{node_id}/metadata"
    body = [{
        "key": "lat", "value": "29.9792",
    }, {
        "key": "lon", "value": "31.1342",
    }]
    resp = requests.post(url, json=body, headers=header)
    if resp.status_code == 204:
        print("Success")
    else:
        print("Error")
else:
    print("Error")
```

This step can the be repeated for each indoor sensor Node.

## Assigning an existing Indoor Sensor as a child of a specific Building Node

To assign an existing Indoor Sensor as a child of a Building Node, send a PUT request to the `/{domain}/api/v1/nodes/{node_id}` endpoint.

The only thing we need to change is the `parent` field.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
parent_node_id = 1931
child_node_id = 1941
url = f"http://canary.lvh.me/{domain}/api/v1/nodes/{child_node_id}"

body = {
  "parent": parent_node_id,
}

reply = requests.put(url, json=body, headers=header)
if reply.status_code == 204:
    print("Success")
else:
    print("Error")
```


---
priority: 50
---

# Activate the Building Service

[Back to index](/index.html)

This guide demonstrates how to create and deploy a service using the EnergyView API v1.

For more information about the API, refer to the online [API documentation](https://customer.noda.se/api/v1).

## Prerequisites

An API key is required to interact with the API. If you have sufficient privileges, you can create an API key through the EnergyView web interface. Contact your system administrator if you do not have the necessary privileges.

Each request is made to `https://customer.noda.se/{domain}/api/v1/...`, where `{domain}` is the domain name of your EnergyView instance. A customer may have multiple domains, each managed by a separate database. This item is also sometimes referred to as "site".

## Create a Control Node

The initial step is to create a Control Node, which represents a single heating or cooling system. This node contains all the settings and data needed for the algorithms to function properly.

To create a Control Node, send a POST request to the `/{domain}/api/v1/nodes` endpoint.

The request body should be in JSON format. Here's an example of a valid request body:

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"http://canary.lvh.me/{domain}/api/v1/nodes"

body = {
  "name": "My Control Node",
  "designation": "building",
  "description": "My Control Node for my building",
  "dataif": "optional string used as an identifier",
  "tags": [
    "operational_state",
    "outdoortemp",
    "outdoortemp_fake",
    "outdoortemp_offset",
    "returntemp_sec",
    "supplytemp_sec",
    "supplytemp_sec_controller_setvalue",
    "supplytemp_sec_offset",
    "meter_effect",
    "meter_heatenergy",
    "meter_primreturntemp",
    "meter_primsupplytemp",
    "meter_volume",
    "meter_volumeflow",
  ],
  "device": "Kelp-Basic",
  "state": "pre-installation"
}

response = requests.post(url, json=body, headers=header)
print(response.json())  # {'id': 123, 'uuid': '12345678-1234-1234-1234-123456789012'}
```
```json
{
  "uuid": "12345678-1234-1234-1234-123456789012",
  "name": "My Control Node",
  "designation": "building",
  "description": "My Control Node for my building",
  "dataif": "optional string used as an identifier",
  "tags": [
    "operational_state",
    "outdoortemp",
    "outdoortemp_fake",
    "outdoortemp_offset",
    "returntemp_sec",
    "supplytemp_sec",
    "supplytemp_sec_controller_setvalue",
    "supplytemp_sec_offset",
    "meter_effect",
    "meter_heatenergy",
    "meter_primreturntemp",
    "meter_primsupplytemp",
    "meter_volume",
    "meter_volumeflow",
  ],
  "device": "ControlNode",
  "state": "pre-installation"
}
```

Table of the fields in the request body:


| Field | Description |
| --- | --- |
| `uuid` | (optional) The requested UUID of the Node. If not specified, a random UUID will be generated. This can be used to assign a specific UUID to a Node. |
| `name` | The name of the Node. |
| `designation` | The Node's designation, such as building, heating system, indoor climate sensor, etc. |
| `description` | A description of the Node. |
| `dataif` | An optional string that can be used as a secondary way to identify the Node. |
| `tags` | A list of tags that can be used to identify the Node. This includes the complete list of sensors we want to enable on the Node. The system manages a fixed list of tags for different devices. |
| `device` | The device type of the Node. |
| `state` | The state of the Node. |


The response will be a `201 Created`, and the response body will contain the created Node's serial ID and UUID.

```json
{
  "id": 123,
  "uuid": "12345678-1234-1234-1234-123456789012"
}
```

Save the serial ID or UUID of the created Node, as they will be used in the next step.


## Create Climate Sensor Nodes

Next, create Climate Sensor Nodes. These nodes represent individual indoor climate sensors and will be associated with a Control Node.

To create Climate Sensor Nodes, send a POST request to the `/{domain}/api/v1/nodes` endpoint for each node.

The request body should be in JSON format. Here's an example of a valid request body:

```json
{
  "uuid": "cafe1234-cafe-cafe-cafe-cafe12345678",
  "name": "My Climate Sensor Node #1",
  "designation": "sensor/indoor",
  "description": "One of several climate sensors",
  "dataif": "optional string used as an identifier",
  "tags": [
   "indoortemp"
  ],
  "parent": "12345678-1234-1234-1234-123456789012",
  "device": "Generic Indoor Sensor",
  "state": "pre-installation"
}
```

The description of the fields in the request body is the same as for the Control Node, with one exception: `parent` is a required field specifying the serial ID or UUID of the Control Node to associate the Climate Sensor Node with.

The response will be a `201 Created`, and the response body will contain the created Node's serial ID and UUID.

```json
{
  "id": 124,
  "uuid": "cafe1234-cafe-cafe-cafe-cafe12345678"
}
```

Repeat this process for each Climate Sensor Node you want to create.


## Deploy the Service

The final step is to deploy the service on the Control Node, allowing the algorithms to start running.

To deploy the service, send a POST request to the `/{domain}/api/v1/nodes/{id}/provision` endpoint, where `{id}` is the serial ID of the Control Node.

The request body should be in JSON format. Here's an example of a valid request body:

```json
{
  "active": true,
  "balance_temperature": 17,
  "idt_wanted": 21,
  "idt_min": 17
}
```

Table of the fields in the request body:

| Field | Description |
| --- | --- |
| `active` | Whether the service should be active or not. |
| `balance_temperature` | The balance temperature of the system, typically the outdoor temperature at which the pump is turned off. |
| `idt_wanted` | The desired average indoor temperature for the cluster of climate sensors. |
| `idt_min` | The minimum allowed indoor temperature for any indoor climate sensor. |

The response will be a `204 No Content`, and the response body will be empty.


## Update the Service

To update a running service, repeat the process described in the previous section. The service will be updated with the new settings.

Set the `active` field to `false` to stop the service.

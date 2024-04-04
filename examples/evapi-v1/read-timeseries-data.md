---
priority: 30
---
# Read TimeSeries data

[Back to index](/index.html)

The ability to read or extract TimeSeries data via requests is the second most important function of the EnergyView API. It is only preceded by the function to store data in the database.

We designed the TimeSeries API to be as easy to use as possible while allowing for more complex use cases.

> **NOTE**: It is essential to escape certain characters that are part of the URL. The `+`, for example, is used to indicate a space in a URL. Suppose you do not escape the `+` in, for instance, an RFC3339 timestamp. Then, the format will be treated as invalid once parsed by the server.  
> Whether you are required to escape the character manually or if the HTTP library you are using does this depends on the library's functionality.


## Basic example with a single tag

In the following example we extract data from a single tag on a single node.

To allow for more complex use-cases, the id of a Node can be either an `integer` or a `UUID`.

We need to specify the following;

- *node_id*, the unique identifier for the node we want to extract data from.
- *tag*, the name of the tag we want to extract data fromm which belongs to the node.
- *start*, the start date and time for the data we want to extract. The format is [RFC3339](/various/rfc3339.html).
- *end*, the end date and time for the data we want to extract. The format is [RFC3339](/various/rfc3339.html).

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

params = {
    "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
    "tag": "outdoortemp",
    "start": "2023-01-01T00:00:00+01:00",
    "end": "2023-01-02T00:00:00+01:00"
}

reply = requests.get(url, headers=header, params=params)

print(reply.json())
```
```shell
curl -X GET \
     -H "Authorization: Key demo-secret" \
    -H "Accept: application/json" \
    -d '{"node_id":"be65cf3b-dec1-479f-981f-54157d8588ff","tag":"outdoortemp","start":"2023-01-01T00:00:00+01:00","end":"2023-01-02T00:00:00+01:00"}' \
    https://customer.noda.se/demo/api/v1/timeseries
```

The format of the returned data is a JSON array of objects with the following fields:

```json
{
  "timeseries": [
    {
        "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
        "tag": "outdoortemp",
        "data": [
            {
                "v": 3.14,
                "ts": "2020-01-01T00:00:00+01:00"
            },
            {
                "v": 3.15,
                "ts": "2020-01-01T01:00:00+01:00"
            },
            {
                "v": 3.16,
                "ts": "2020-01-01T02:00:00+01:00"
            },
            {
                "v": 3.17,
                "ts": "2020-01-01T03:00:00+01:00"
            },
            ...
        ]
    }
  ]
}
```

As you can see, the data is returned as a JSON array of objects. Each object contains the `node_id`, the `tag` and the `data` for that specific tag. The purpose of the array is to allow for multiple tags to be returned in a single request.


## Basic example with multiple tags

In the following example, we extract data from multiple tags on multiple nodes.

To allow for more complex use-cases, the id of a Node can be either an `integer` or a `UUID`.

We need to specify the following;

- *node_ids*, the unique identifier for the nodes we want to extract data from.
- *tags*, the names of the tags we want to extract data from which belongs to the node.
- *start*, the start date and time for the data we want to extract. The format is [RFC3339](/various/rfc3339.html).
- *end*, the end date and time for the data we want to extract. The format is [RFC3339](/various/rfc3339.html).

```python
import json
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

params = {
    "node_ids": json.dumps([
            "be65cf3b-dec1-479f-981f-54157d8588ff",
            "64c1faf9-b23c-4f6d-9429-b2b3f5e4811d"
        ]),
    "tags": json.dumps([
            "outdoortemp",
            "supplytemp_sec",
            "returntemp_sec"
        ]),
    "start": "2023-01-01T00:00:00+01:00",
    "end": "2023-01-02T00:00:00+01:00"
}

reply = requests.get(url, headers=header, params=params)

print(reply.json())
```


The format of the returned data is the same as for the first Basic example with a single tag. The only difference is that there will be several objects inside the timeseries array:

```json
{
  "timeseries": [
    {
        "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
        "tag": "outdoortemp",
        "data": [
            {
                "v": 3.14,
                "ts": "2020-01-01T00:00:00+01:00"
            },
            {
                "v": 3.15,
                "ts": "2020-01-01T01:00:00+01:00"
            },
            {
                "v": 3.16,
                "ts": "2020-01-01T02:00:00+01:00"
            },
            {
                "v": 3.17,
                "ts": "2020-01-01T03:00:00+01:00"
            },
            ...
        ]
    },
    {
        "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
        "tag": "supplytemp_sec",
        "data": [
            {
                "v": 87,
                "ts": "2020-01-01T00:00:00+01:00"
            },
            {
                "v": 88,
                "ts": "2020-01-01T01:00:00+01:00"
            },
            {
                "v": 86,
                "ts": "2020-01-01T02:00:00+01:00"
            },
            {
                "v": 85,
                "ts": "2020-01-01T03:00:00+01:00"
            },
            ...   
        ]
    }
}
```

## Advanced example

In the following example we extract data from a single node and a single tag while also specifying the aggregation method.

For aggregation of data to work we need to truncate the timestamps to the desired resolution, we also need to supply the aggregation method.

- `resolution`, the resolution of the timestamps. Available options are;
  + second
  + minute
  + 5minute
  + 10minute
  + 15minute
  + 20minute
  + 30minute
  + hour
  + day
  + month
  + year
  + decade
  + century
  + millennia
- `aggregate`, the aggregation method. Available options are;
  + avg
  + min
  + max
  + sum
  + count

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

data = {
    "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
    "tag": "outdoortemp",
    "start": "2023-01-01T00:00:00+01:00",
    "end": "2023-02-01T00:00:00+01:00",
    "resolution": "day",
    "aggregate": "avg"
}

reply = requests.get(url, headers=header, params=params)

print(reply.json())
```

Using aggregation will return computed values for the specified resolution.

To get the minimum value for each day we would use the following request:

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

params = {
    "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
    "tag": "outdoortemp",
    "start": "2023-01-01T00:00:00+01:00",
    "end": "2023-02-01T00:00:00+01:00",
    "resolution": "day",
    "aggregate": "min"
}

reply = requests.get(url, headers=header, params=params)

print(reply.json())
```


## Epoch format

The API also supports the UNIX epoch format for timestamps.

To use the UNIX epoch format we need to specify the `epoch` parameter.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {"Authorization": f"Key {secret}"}
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

params = {
    "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
    "tag": "outdoortemp",
    "start": "2023-01-01T00:00:00+01:00",
    "end": "2023-02-01T00:00:00+01:00",
    "epoch": 1
}

reply = requests.get(url, headers=header, params=params)

print(reply.json())
```

Instead of timestamps in RFC3339 format, all timestamp will now use the number of seconds since the UNIX epoch (January 1st 1970).

```json
{
  "timeseries": [
    {
        "node_id": "be65cf3b-dec1-479f-981f-54157d8588ff",
        "tag": "outdoortemp",
        "data": [
            {
                "v": 3.14,
                "ts": 1640995200
            },
            {
                "v": 3.15,
                "ts": 1641081600
            },
            {
                "v": 3.16,
                "ts": 1641168000
            },
            {
                "v": 3.17,
                "ts": 1641254400
            },
            ...
        ]
    }
}
```

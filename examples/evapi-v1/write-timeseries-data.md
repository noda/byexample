---
priority: 3
---
# Write TimeSeries data

[Back to index](/index.html)

The ability to store TimeSeries data via requests is one of the main purposes of the EnergyView API. It is the foundation of the EnergyView system.


## Basic example with a single tag

In the following example we store data for a single tag on a single node.

To allow for more complex use-cases, the id of a Node can be either an `integer` or a `UUID`.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {
    "Authorization": f"Key {secret}",
    "Content-Type": "application/json",
}
params = {"silent": "true"}    # 204 No Content
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

data = [
    {
        "node_id": 1,
        "tag": "outdoortemp",
        "data": [
            {"v": 12.3, "ts": "2023-01-01T12:00:00Z"},
            {"v": 12.4, "ts": "2023-01-01T12:10:00Z"},
            {"v": 12.5, "ts": "2023-01-01T12:20:00Z"},
        ],
    }
]

reply = requests.post(url, headers=header, params=params, json=data)
if reply.status_code == 204:
    print("OK")
else:
    print("Error")
```
```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
)

func main() {
    domain := "demo"
    secret := "demo-secret"
    headers := map[string]string{
        "Authorization": "Key " + secret,
        "Content-Type":  "application/json",
    }
    params := "silent=true" // 204 No Content
    url := fmt.Sprintf("https://customer.noda.se/%s/api/v1/timeseries?%s", domain, params)

    data := []map[string]interface{}{
        {
            "node_id": 1,
            "tag":     "outdoortemp",
            "data": []map[string]interface{}{
                {"v": 12.3, "ts": "2023-01-01T12:00:00Z"},
                {"v": 12.4, "ts": "2023-01-01T12:10:00Z"},
                {"v": 12.5, "ts": "2023-01-01T12:20:00Z"},
            },
        },
    }

    dataBytes, err := json.Marshal(data)
    if err != nil {
        panic(err)
    }

    req, err := http.NewRequest("POST", url, bytes.NewBuffer(dataBytes))
    if err != nil {
        panic(err)
    }

    for key, value := range headers {
        req.Header.Set(key, value)
    }

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    if resp.StatusCode == 204 {
        fmt.Println("OK")
    } else {
        fmt.Println("Error")
    }
}
```


## Basic example with multiple tags and nodes

The code is the same as above, the only difference is that we add more data points.

```python
data = [
    {
        "node_id": 1,
        "tag": "outdoortemp",
        "data": [
            {"v": 12.3, "ts": "2023-01-01T12:00:00Z"}
        ],
    },
    {
        "node_id": 2,
        "tag": "outdoortemp",
        "data": [
            {"v": 0.5, "ts": "2023-01-01T12:00:00Z"}
        ],
    },
    {
        "node_id": "12345678-1234-1234-1234-123456789012",
        "tag": "outdoortemp",
        "data": [
            {"v": 12.3, "ts": "2023-01-01T12:00:00Z"}
        ],
    }
]
```

As you can see, the `node_id` can be either an `integer` or a `UUID`.


## Overwrite existing data

The `overwrite` parameter can be used to overwrite existing data points.

> *NOTE*: You are replacing data when doing this. So be sure that you know what you are doing.

```python
import requests

domain = "demo"
secret = "demo-secret"
header = {
    "Authorization": f"Key {secret}",
    "Content-Type": "application/json",
}
params = {"silent": "true"}    # 204 No Content
url = f"https://customer.noda.se/{domain}/api/v1/timeseries"

# Add the overwrite parameter to params
params = {
    "silent": "true",
    "overwrite": "replace_window",
}

data = [
    {
        "node_id": 1,
        "tag": "outdoortemp",
        "data": [
            {
             "v": 12.3,
             "ts": "2023-01-01T12:00:00Z"    # This marks the start of the window
            },
            {
                "v": 12.4,
                "ts": "2023-01-01T12:10:00Z"
            },
            {
                "v": 12.5,
                "ts": "2023-01-01T12:20:00Z"    # This marks the end of the window
            }
        ],
    }
]

reply = requests.post(url, headers=header, params=params, json=data)
if reply.status_code == 204:
    print("OK")
else:
    print("Error")
```

The possible values for `overwrite` are:

- `replace_window` - Delete the window (start and end timestamp of the data points) and insert new data 
- `update_window` - Only insert new data points, update existing data points at the same timestamp with new values

<!--
    
 * @OA\Schema(
 *     schema="TimeseriesList",
 *     type="object",
 *     @OA\Property(
 *    property="timeseries",
 *    type="array",
 *    @OA\Items(ref="#/components/schemas/Timeseries")
 *    )
 * )
 * 
 * @OA\Schema(
 *     schema="Timeseries",
 *     type="object",
 *     @OA\Property(property="node_id", type="integer", description="Node ID"),
 *     @OA\Property(property="tag", type="string", description="Tag"),
 *     @OA\Property(property="data", type="array", description="Data", @OA\Items(ref="#/components/schemas/TimeseriesData")),
 * )
 * 
 * @OA\Schema(
 *     schema="TimeseriesData",
 *     type="object",
 *        @OA\Property(property="v", type="number", description="Value"),
 *     @OA\Property(property="ts", type="string", description="Timestamp in RFC3339 format"),
 * )

     * @OA\Post(
     *     path="/timeseries",
     *     tags={"timeseries"},
     *     summary="Insert data into existing timeseries",
     *     @OA\RequestBody(
     *     description="Insert timeseries data",
     *     required=true,
     *     @OA\MediaType(
     *         mediaType="application/json",
     *         @OA\Schema(
     *         type="array",
     *         description="Insert multiple timeseries data points",
     *         @OA\Items(
     *             required={"tag", "data"},
     *             @OA\Property(property="node_id", type="string", description="Node ID, should not be supplied together with node_uuid", example="123"),
     *             @OA\Property(property="node_uuid", type="string", description="Node UUID, should not be supplied together with node_id", example="12345678-1234-1234-1234-123456789012"),
     *                @OA\Property(property="tag", type="string", description="Tag (sensor) name", example="outdoortemp"),
     *             @OA\Property(property="data", type="array", description="Array of data points", @OA\Items(ref="#/components/schemas/TimeseriesData"))
     *         )
     *         )
     *     ),
     *     @OA\MediaType(
     *         mediaType="application/x-www-form-urlencoded",
     *         @OA\Schema(
     *         description="Insert a single timeseries data point",
     *         required={"node_id", "tag", "val", "ts"},
     *         @OA\Property(property="node_id", type="string", description="Node ID, should not be supplied together with node_uuid", example="123"),
     *         @OA\Property(property="node_uuid", type="string", description="Node UUID, should not be supplied together with node_id", example="12345678-1234-1234-1234-123456789012"),
     *         @OA\Property(property="tag", type="string", description="Tag (sensor) name", example="outdoortemp"),
     *         @OA\Property(property="val", type="number", description="Value", example="12.3"),
     *         @OA\Property(property="ts", type="date-time", description="Timestamp in RFC3339 format", example="2019-01-01T12:00:00Z")
     *         )
     *         ),
     *     ),
     *     @OA\Parameter(
     *     name="overwrite",
     *     in="query",
     *     description="Overwrite existing data points. A replace will delete the window and insert new data. An update will only insert new data points. The window is defined by the earliest timestamp and the latest timestamp of the data points.",
     *     required=false,
     *     @OA\Schema(
     *         type="string",
     *         enum={"replace_window", "update_window"},
     *     )
     *     ),
     *     @OA\Parameter(
     *     name="silent",
     *     in="query",
     *     description="Do not return any data",
     *     required=false,
     *     @OA\Schema(
     *         type="string",
     *         enum={"true", "false"},
     *     )
     *     ),
     *     @OA\Response(response="200", description="OK", @OA\JsonContent(type="array", @OA\Items(ref="#/components/schemas/Timeseries"))),
     *     @OA\Response(response="204", description="No Content"),
     *     @OA\Response(response="400", description="Bad Request"),
     *     @OA\Response(response="401", description="Unauthorized"),
     *     @OA\Response(response="403", description="Forbidden"),
     * )
     * 
     * @param \Base $f3
     *
     * @SuppressWarnings(PHPMD.StaticAccess)
     *
-->

# EnergyView API: Write TimeSeries data

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

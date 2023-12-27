# Updating TimeSeries Data

[Back to index](/index.html)

This guide will demonstrate how to update an existing TimeSeries with new data points in EnergyView API v2. This process is crucial for maintaining current and accurate data within your system.

For detailed API information, refer to the [API documentation](https://customer.noda.se/api/v2).

## Overview

Updating a TimeSeries involves adding new data points, each consisting of a value and a corresponding timestamp.

## Steps to Update TimeSeries Data

1. **Prepare the Data:** Compile the data points you want to add. Each data point should include a timestamp and its associated value.
2. **Choose the TimeSeries:** Identify the TimeSeries you wish to update by its UUID.
3. **Send the Update Request:** Use a POST request to the specific TimeSeries endpoint with the new data points.
4. **Verify the Update:** Ensure that the data points have been added correctly by retrieving the updated TimeSeries data.

Examples in multiple programming languages will be provided to demonstrate this process.

```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries/{uuid}/data"
header = {"Authorization": "Basic <base64-encoded credentials>"}
data_points = [
    {"timestamp": "2023-07-01T00:00:00Z", "value": 23.5},
    {"timestamp": "2023-07-01T01:00:00Z", "value": 24.0}
]

response = requests.post(api_url, json=data_points, headers=header)
print(response.status_code, response.json())
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries/{uuid}/data';
const headers = { Authorization: 'Basic <base64-encoded credentials>' };
const data_points = [
  { timestamp: '2023-07-01T00:00:00Z', value: 23.5 },
  { timestamp: '2023-07-01T01:00:00Z', value: 24.0 }
];

axios.post(api_url, data_points, { headers })
  .then(response => console.log(response.status, response.data))
  .catch(error => console.error(error));
```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;

public class Main {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://customer.noda.se/api/v2/timeseries/{uuid}/data");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Basic <base64-encoded credentials>");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInputString = "[{\"timestamp\": \"2023-07-01T00:00:00Z\", \"value\": 23.5}, {\"timestamp\": \"2023-07-01T01:00:00Z\", \"value\": 24.0}]";

            try(OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);           
            }

            System.out.println(conn.getResponseCode());
            System.out.println(conn.getResponseMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Text;

class Program
{
    static async Task Main()
    {
        var client = new HttpClient();
        var byteArray = Encoding.ASCII.GetBytes("<base64-encoded credentials>");
        client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", Convert.ToBase64String(byteArray));

        var data_points = new[]
        {
            new { timestamp = "2023-07-01T00:00:00Z", value = 23.5 },
            new { timestamp = "2023-07-01T01:00:00Z", value = 24.0 }
        };

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(data_points);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await client.PostAsync("https://customer.noda.se/api/v2/timeseries/{uuid}/data", content);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

For further guidance see the [OpenAPI specification](https://customer.noda.se/api/v2).
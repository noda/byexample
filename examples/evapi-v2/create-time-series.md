# Creating a TimeSeries

[Back to index](/index.html)

This guide outlines the steps to create a new TimeSeries using EnergyView API v2. 

For comprehensive API details, visit the [API documentation](https://customer.noda.se/api/v2).

## Overview

Creating a TimeSeries involves specifying various attributes, including the name, associated Thing UUID, SI unit, and value boundaries. This process is essential for adding new data streams to monitor and analyze within your system.

## Step-by-Step Guide

1. **Prepare the Request:** Set up your request with the necessary headers and body content. The body should include the TimeSeries name, the UUID of the Thing it's associated with, the SI unit, and the lower and upper bounds for the values.

2. **Send the Request:** Use a POST request to the TimeSeries endpoint (`/api/v2/timeseries`) with the prepared data.

3. **Handle the Response:** Upon success, the API will return details of the created TimeSeries, including its UUID.

Below are examples in multiple programming languages demonstrating how to create a TimeSeries:


```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries"
header = {"Authorization": "Basic <base64-encoded credentials>"}

body = {
    "name": "New TimeSeries",
    "thing_uuid": "uuid-of-associated-thing",
    "si_unit": "C",
    "lower_bound": -50,
    "upper_bound": 50,
    "tags": ["tag1", "tag2"]
}

response = requests.post(api_url, json=body, headers=header)
print(response.json())
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries';
const headers = { Authorization: 'Basic <base64-encoded credentials>' };
const data = {
  name: 'New TimeSeries',
  thing_uuid: 'uuid-of-associated-thing',
  si_unit: 'C',
  lower_bound: -50,
  upper_bound: 50,
  tags: ['tag1', 'tag2']
};

axios.post(api_url, data, { headers })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));

```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;

public class Main {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://customer.noda.se/api/v2/timeseries");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Basic <base64-encoded credentials>");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInputString = "{\"name\": \"New TimeSeries\", \"thing_uuid\": \"uuid-of-associated-thing\", \"si_unit\": \"C\", \"lower_bound\": -50, \"upper_bound\": 50, \"tags\": [\"tag1\", \"tag2\"]}";

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
        var byteArray = System.Text.Encoding.ASCII.GetBytes("<base64-encoded credentials>");
        client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", Convert.ToBase64String(byteArray));

        var data = new
        {
            name = "New TimeSeries",
            thing_uuid = "uuid-of-associated-thing",
            si_unit = "C",
            lower_bound = -50,
            upper_bound = 50,
            tags = new[] { "tag1", "tag2" }
        };

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(data);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await client.PostAsync("https://customer.noda.se/api/v2/timeseries", content);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

For further guidance see the [OpenAPI specification](https://customer.noda.se/api/v2).
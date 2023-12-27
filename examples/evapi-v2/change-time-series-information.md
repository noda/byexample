# Change Time-series Information

[Back to index](/index.html)

This section will guide you through updating the metadata of a Time-series in EnergyView API v2. 

## Overview

Updating a Time-series involves modifying its attributes like name, bounds, or tags. This functionality is essential for keeping the Time-series relevant and accurately described.

## Steps for Updating Time-series Information

1. **Identify the Time-series:** Use the UUID of the Time-series you want to update.
2. **Prepare the Update Data:** Formulate the data representing the updates, which may include changes to the name, bounds, and tags.
3. **Send the Update Request:** Execute a PUT request to the Time-series endpoint with the new data.
4. **Verify the Update:** Confirm the changes by retrieving the Time-series details again.

Examples in multiple programming languages will be provided to demonstrate this process.

```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries/{uuid}"
header = {"Authorization": "Basic <base64-encoded credentials>"}
update_data = {
    "name": "Updated Time-series Name",
    "lower_bound": -40,
    "upper_bound": 60,
    "tags": ["updatedTag1", "updatedTag2"]
}

response = requests.put(api_url, json=update_data, headers=header)
print(response.status_code)
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries/{uuid}';
const headers = { Authorization: 'Basic <base64-encoded credentials>' };
const update_data = {
  name: 'Updated Time-series Name',
  lower_bound: -40,
  upper_bound: 60,
  tags: ['updatedTag1', 'updatedTag2']
};

axios.put(api_url, update_data, { headers })
  .then(response => console.log(response.status))
  .catch(error => console.error(error));
```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://customer.noda.se/api/v2/timeseries/{uuid}");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("PUT");
            conn.setRequestProperty("Authorization", "Basic <base64-encoded credentials>");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInputString = "{\"name\": \"Updated Time-series Name\", \"lower_bound\": -40, \"upper_bound\": 60, \"tags\": [\"updatedTag1\", \"updatedTag2\"]}";

            try(OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
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

        var data = new
        {
            name = "Updated Time-series Name",
            lower_bound = -40,
            upper_bound = 60,
            tags = new[] { "updatedTag1", "updatedTag2" }
        };

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(data);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await client.PutAsync("https://customer.noda.se/api/v2/timeseries/{uuid}", content);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```
# Deleting Data from a TimeSeries

[Back to index](/index.html)

This guide will illustrate how to delete specific data points from a TimeSeries in the EnergyView API v2.

## Process Overview

1. **Identify the Data Points:** Determine the specific data points in the TimeSeries you want to delete, typically defined by their timestamps.
2. **Prepare the Request:** Formulate a DELETE request with the necessary parameters, like the TimeSeries UUID and the range or specific data points to be deleted.
3. **Send the Request:** Execute the DELETE request to the specified endpoint for the TimeSeries.
4. **Confirm Deletion:** Ensure the data points have been successfully deleted by retrieving the TimeSeries data again.

```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries/{uuid}/data"
params = {
    "start": "2023-01-01T00:00:00Z",
    "end": "2023-01-02T00:00:00Z"
}
header = {"Authorization": "Basic <base64-encoded credentials>"}

response = requests.delete(api_url, params=params, headers=header)
print(response.status_code)
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries/{uuid}/data';
const params = {
  start: '2023-01-01T00:00:00Z',
  end: '2023-01-02T00:00:00Z'
};
const headers = { Authorization: 'Basic <base64-encoded credentials>' };

axios.delete(api_url, { params, headers })
  .then(response => console.log(response.status))
  .catch(error => console.error(error));
```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        try {
            String start = URLEncoder.encode("2023-01-01T00:00:00+01:00", StandardCharsets.UTF_8.toString());
            String end = URLEncoder.encode("2023-01-02T00:00:00+01:00", StandardCharsets.UTF_8.toString());

            URL url = new URL("https://customer.noda.se/api/v2/timeseries/{uuid}/data?start=" + start + "&end=" + end);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("DELETE");
            conn.setRequestProperty("Authorization", "Basic <base64-encoded credentials>");

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

class Program
{
    static async Task Main()
    {
        var client = new HttpClient();
        var byteArray = System.Text.Encoding.ASCII.GetBytes("<base64-encoded credentials>");
        client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Basic", Convert.ToBase64String(byteArray));

        var start = Uri.EscapeDataString("2023-01-01T00:00:00+01:00");
        var end = Uri.EscapeDataString("2023-01-02T00:00:00+01:00");
        var url = $"https://customer.noda.se/api/v2/timeseries/{{uuid}}/data?start={start}&end={end}";

        HttpResponseMessage response = await client.DeleteAsync(url);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}

```
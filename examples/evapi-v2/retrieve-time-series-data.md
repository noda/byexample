# Retrieving Data from a TimeSeries

[Back to index](/index.html)

This guide covers how to retrieve data from a TimeSeries in EnergyView API v2, a crucial step for data analysis and monitoring.

## Process Overview

1. **Identify the TimeSeries:** Use the UUID of the TimeSeries you want to access.
2. **Configure the Request:** Set up a GET request with necessary parameters, such as time range and format.
3. **Execute the Request:** Send the GET request to the TimeSeries data endpoint.
4. **Handle the Response:** The API will return the requested data points.

Here are examples in various languages:

```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries/{uuid}/data"
params = {
    "start": "2023-01-01T00:00:00Z",
    "end": "2023-01-02T00:00:00Z",
    "aggregate": "avg"
}
header = {"Authorization": "Basic <base64-encoded credentials>"}

response = requests.get(api_url, params=params, headers=header)
print(response.json())
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries/{uuid}/data';
const params = {
  start: '2023-01-01T00:00:00Z',
  end: '2023-01-02T00:00:00Z',
  aggregate: 'avg'
};
const headers = { Authorization: 'Basic <base64-encoded credentials>' };

axios.get(api_url, { params, headers })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            String start = URLEncoder.encode("2023-01-01T00:00:00Z", StandardCharsets.UTF_8.toString());
            String end = URLEncoder.encode("2023-01-02T00:00:00Z", StandardCharsets.UTF_8.toString());
            String aggregate = URLEncoder.encode("avg", StandardCharsets.UTF_8.toString());

            URL url = new URL("https://customer.noda.se/api/v2/timeseries/{uuid}/data?start=" + start + "&end=" + end + "&aggregate=" + aggregate);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Authorization", "Basic <base64-encoded credentials>");

            Scanner sc = new Scanner(url.openStream());
            while(sc.hasNext()) {
                System.out.println(sc.nextLine());
            }
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

        var start = Uri.EscapeDataString("2023-01-01T00:00:00Z");
        var end = Uri.EscapeDataString("2023-01-02T00:00:00Z");
        var aggregate = Uri.EscapeDataString("avg");
        var url = $"https://customer.noda.se/api/v2/timeseries/{{uuid}}/data?start={start}&end={end}&aggregate={aggregate}";

        HttpResponseMessage response = await client.GetAsync(url);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

Replace `{uuid}` with the actual UUID of the TimeSeries.

Here's a table summarizing the query parameters for retrieving data from a TimeSeries in EnergyView API v2:

| Parameter   | Description                                | Format         | Example Value         |
|-------------|--------------------------------------------|----------------|-----------------------|
| `start`     | Start date/time                            | RFC3339        | `2023-01-01T00:00:00Z`|
| `end`       | End date/time                              | RFC3339        | `2023-01-02T00:00:00Z`|
| `unit`      | Unit for data conversion                   | String         | `"C"`                 |
| `ge`        | Greater than/equal to value                | Numeric        | `10`                  |
| `le`        | Less than/equal to value                   | Numeric        | `20`                  |
| `precision` | Precision of returned data                 | String         | `"hour"`              |
| `aggregate` | Aggregate function (avg, min, max)         | String         | `"avg"`               |
| `timezone`  | Timezone for data                          | String         | `"Europe/Stockholm"`  |


For further guidance see the [OpenAPI specification](https://customer.noda.se/api/v2).
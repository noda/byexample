# Listing TimeSeries

[Back to index](/index.html)

This guide demonstrates how to list TimeSeries in the EnergyView API v2.

For comprehensive details, refer to the [API documentation](https://customer.noda.se/api/v2).

## Basic Use Case

Imagine you need to retrieve a list of all TimeSeries related to a specific building or energy system. This process involves sending a GET request to the appropriate API endpoint.

Below are examples in multiple programming languages demonstrating how to list TimeSeries:

```python
import requests

api_url = "https://customer.noda.se/api/v2/timeseries"
header = {"Authorization": "Basic <base64-encoded credentials>"}

response = requests.get(api_url, headers=header)
time_series_list = response.json()

for series in time_series_list:
    print(series['name'], series['uuid'])
```
```javascript
// Node.js
const axios = require('axios');

const api_url = 'https://customer.noda.se/api/v2/timeseries';
const headers = { Authorization: 'Basic <base64-encoded credentials>' };

axios.get(api_url, { headers })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));

```
```java
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://customer.noda.se/api/v2/timeseries");
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

        HttpResponseMessage response = await client.GetAsync("https://customer.noda.se/api/v2/timeseries");
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

This script will output the name and UUID of each TimeSeries, allowing you to identify and work with specific data streams. 

For further guidance see the [OpenAPI specification](https://customer.noda.se/api/v2).

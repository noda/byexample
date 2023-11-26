---
priority: 20
---
# Update Node Settings

[Back to index](/index.html)

This guide demonstrates how to update the settings of a Node using the EnergyView API v1.

For more information about the API, refer to the online [API documentation](https://customer.noda.se/api/v1).

## A Basic Use Case

Imagine you want to update the settings of a Building Node, particularly changing its operational parameters. For example, adjusting the balance temperature setting for a heating system.

To update this setting, send a PUT request to the `/{domain}/api/v1/settings/{type}/{id}` endpoint.

The key elements for the request are:

- The type of setting (e.g., 'node').
- The ID of the node whose settings you want to update.
- The specific setting you wish to change (e.g., 'balance_temperature').

Here's how you might perform this operation:

```python
import requests

domain = "demo"
node_id = 123  # Replace with your Node ID
setting_type = "node"
setting_path = "coco.default.control.balance_temperature"
new_value = 20  # New balance temperature value

url = f"http://canary.lvh.me/{domain}/api/v1/settings/{setting_type}/{node_id}"
header = {"Authorization": "Key YOUR_API_KEY"}
body = {
    "path": setting_path,
    "value": new_value
}

response = requests.put(url, json=body, headers=header)
if response.status_code == 204:
    print("Setting updated successfully")
else:
    print("Error updating setting")
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
    nodeID := "123"  // Replace with your Node ID
    settingType := "node"
    settingPath := "coco.default.control.balance_temperature"
    newValue := 20  // New balance temperature value

    url := fmt.Sprintf("http://canary.lvh.me/%s/api/v1/settings/%s/%s", domain, settingType, nodeID)

    body := map[string]interface{}{
        "path":  settingPath,
        "value": newValue,
    }
    jsonData, _ := json.Marshal(body)

    req, _ := http.NewRequest("PUT", url, bytes.NewBuffer(jsonData))
    req.Header.Set("Authorization", "Key YOUR_API_KEY")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    if resp.StatusCode == http.StatusNoContent {
        fmt.Println("Setting updated successfully")
    } else {
        fmt.Println("Error updating setting")
    }
}

```

After sending this request, the specified setting for the Building Node will be updated with the new value.

Refer to the [API documentation](https://customer.noda.se/api/v1) for more details on other settings that can be updated and their respective values.
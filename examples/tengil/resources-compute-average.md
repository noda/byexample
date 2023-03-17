# Compute an average for a set of Resources

[Back to index](/index.html)

This example shows how to compute an average for a set of Resources.

First, the Program must have at least one Resource bound to it. This is easily done in the EnergyView UI.

The Program can then access the Resources using the `resources` module.

```tengo
dbstore := import("dbstore")
log := import("log")
resources := import("resources")

// Get all Resources bound to the Program
for node_id, v in resources.GetNodes() {
    // node_id is the integer ID of the Node
    // v is a map of details about the Node on the format;
    // {
    //     id: int64,         // integer ID of the Node
    //     guid: string,      // UUID of the Node
    //     dataif: string,    // Remote resource Identifier
    //     name: string,      // Name of the Node
    //     device: string,    // Device type of the Node
    //     object: string,    // Object type of the Node
    //     sensors: []string, // List of sensor tags
    //     parent: int64,     // Parent Node ID
    //     children: []int64, // List of child Node IDs
    // }

    node_tags := []
    for tag in v.sensors {
        if "outdoortemp" == tag {
            node_tags = append(tags, fmt.sprintf("%d.%s", node_id, tag))
        }
    }
}

total = 0.0
count = 0
for row in dbstore.GetMulti(node_tags) {
    total += row.value
    count += 1
}

if count > 0 {
    avg := total / count
    log.Info(fmt.sprintf("Average is %v", avg))
}
```

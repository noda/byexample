# Tengil: About

Tengil is a Program Manager and script environment which allows for advanced interaction with the data in EnergyView.

Tengil is built upon the [Tengo programming language](https://github.com/d5/tengo), which is a scripting language and engine with syntax similar to Go. The purpose of the solution is to provide an interface for simple computations and ingesting data from external sources.

Some of the built-in modules available in the Tengo engine are disabled in Tengil as security precautions. The following modules are disabled:

- `os`: Platform-independent interface to operating system functionality

The following existing modules are available from the Tengo engine:

- `base64`: Base64 encoding and decoding functions
- `enum`: Enumeration functions
- `fmt`: Formatting functions
- `hex`: Hex encoding and decoding functions
- `json`: JSON functions
- `math`: Mathematical constants and functions
- `rand`: Random functions
- `text`: Regular expressions, string conversion, and manipulation
- `times`: Time-related functions

The following new modules are added by Tengil:

- `alert`: Alert functions to create and send alerts
- `config`: Configuration functions to get and set configuration data
- `dbstore`: Database functions to get and set timeseries data
- `http`: HTTP functions to get, post, put and delete data
- `log`: Logging functions
- `memstore`: Memory functions to store temporary data
- `resources`: Resource functions to get resources bound to a Program

A simple Hello World example of a Tengil program:

```tengo
log := import("log")

log.Info("Hello World!")
```

Or, a more "complex" example:

```tengo
dbstore := import("dbstore")

// Fetch the outdoortemp for Node with ID 1
data := dbstore.Get("1.outdoortemp")

/* Format of data
{
    node_id: 1,
    tag: "outdoortemp",
    timestamp: 2022-01-01 16:13:45.815817 +0100 CET,
    value: 3.14,
    unit: "c"
}
*/
```

Or, an even more "complex" example:

```tengo
dbstore := import("dbstore")

// Fetch the supply and return temperature for Node with ID 1
supplytemp_sec := dbstore.Get("1.supplytemp_sec")
returntemp_sec := dbstore.Get("1.returntemp_sec")

// Find the latest timestamp
ts := supplytemp_sec.timestamp
if returntemp_sec.timestamp > ts {
    ts = returntemp_sec.timestamp
}

// Calculate delta temperature
delta_temp := supplytemp_sec.value - returntemp_sec.value

// Store the delta temperature
dbstore.Set("1.delta_temp", delta_temp, ts)
```

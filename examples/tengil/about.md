# Tengil: About

Tengil is a Program Manager and scripting environment that enables advanced interaction with data in EnergyView.

Built on the [Tengo programming language](https://github.com/d5/tengo), Tengil shares a similar syntax with Go and serves as an interface for basic calculations and data ingestion from external sources.

For security reasons, some built-in Tengo engine modules are disabled in Tengil. The disabled modules include:

- `os`: A platform-independent interface for operating system functionality

Tengil supports the following existing Tengo engine modules:

- `base64`: Functions for encoding and decoding Base64
- `enum`: Enumeration functions
- `fmt`: Formatting functions
- `hex`: Functions for encoding and decoding Hex
- `json`: JSON functions
- `math`: Mathematical constants and functions
- `rand`: Random functions
- `text`: Regular expressions, string conversion, and manipulation
- `times`: Time-related functions

Additionally, Tengil introduces the following new modules:

- `alert`: Functions to create and send alerts
- `config`: Functions to get and set configuration data
- `dbstore`: Functions to get and set timeseries data in the database
- `http`: Functions to get, post, put, and delete data via HTTP
- `log`: Logging functions
- `memstore`: Functions for temporary data storage in memory
- `resources`: Functions to access EnergyView resources associated with a Program

A simple "Hello World" example of a Tengil program:

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

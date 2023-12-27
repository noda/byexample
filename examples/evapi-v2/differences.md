---
priority: 0
---
# Differences Between APIv1 and APIv2

[Back to index](/index.html)

APIv2, unlike its predecessor, is built on a distinct information model. It emphasizes unique time series linked to Things - objects representing any entity.

Here's a conceptual mapping between APIv1 and APIv2:

- Node -> Thing
- Time-series -> Time-series
- Dataset -> Dataset

However, the interface has changed significantly, necessitating understanding these differences to utilize APIv2 effectively.

## Authentication

The authentication method in APIv2 differs from APIv1. Previously, authentication was achieved using *Authorization: Key ...*, and the target customer's *domain* was included in the URL. In contrast, APIv2 incorporates the domain into a standard *Basic* authentication format: *Authorization: Basic <base64 domain:secret-key>*.

## UUIDs

APIv1 occasionally permitted the use of UUIDs. In APIv2, UUIDs are mandatory and are exclusive identifiers for Things, time series, and Datasets.

Each Thing, Time-series, and Dataset possesses a unique UUID. There should never be an instance where a UUID is identical for a time series and a Dataset.

For more detailed information on UUIDs and their structure, visit the [UUID Wikipedia page](https://en.wikipedia.org/wiki/Universally_unique_identifier).

## Origin

EnergyView is not the originator of APIv2. It stemmed from a different software - the [NODA Self-host project](https://github.com/self-host/self-host). In this project, Time-series are distinct entities, not necessarily linked to any parent object, like a Thing.

Nevertheless, due to significant design variations between these systems, the APIv2 implementation in EnergyView cannot perfectly mirror the API in the NODA Self-host. For instance, in EnergyView, you must link a time series to a Thing, a constraint not present in the NODA Self-host.

While APIv2 strives to maintain compatibility with the NODA Self-host, the calls and paths are similar, though sometimes different. An API layer developed for the NODA Self-host might require adjustments to function seamlessly with APIv2.

## Missing Features

APIv2 presents a more streamlined interface compared to APIv1, a result of its foundational design. The primary aim of APIv2, along with the NODA Self-host, is to facilitate an interface for machines to store and retrieve time-series values at specific locations as needed.


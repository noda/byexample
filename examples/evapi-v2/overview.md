---
priority: 1
---

# Overview

[Back to index](/index.html)

## Simple Information Model

There are three different objects in the APIv2 model.

- **Time-series:** Represents a single series of time series values. The series can only store two values for any given point: a float value and the time stamp.
- **Things:** The purpose of a Thing is to keep track of time series by grouping them. A Thing can be anything, such as a radiator circuit, an entire heating system, a pump station, etc.
- **Datasets:** A Dataset is just a data document. It allows for the storage of more complex objects than time series allow.

### Time-series

The Time-series object in APIv2 is crucial for storing and managing time-stamped data. It includes several operations:

- **Getting Time-series Data:** You can retrieve all Time-series or specific details of a Time-series using its UUID. 
- **Creating and Updating Time-series:** New Time-series can be created, and existing ones can be updated with new information.
- **Deleting Time-series:** Allows the removal of a Time-series from the system.
- **Data Manipulation:** Features for adding, retrieving, and deleting measurement data associated with a Time-series. This includes specifying parameters such as start and end times, units, and aggregation functions.

Each Time-series is identified by a unique UUID and is associated with a Thing. It stores two values for each data point: a floating-point value and a time stamp. This structure makes it highly suitable for time-dependent data analysis and tracking.

The model of a Time-series is as follows;

- **id:** A unique string identifier for the Time-series, formatted as an ID.
- **thing_uuid:** A string representing the UUID of the associated Thing, which is optional.
- **created_by:** The UUID of the user who created the Time-series.
- **name:** The name of the Time-series.
- **si_unit:** The SI unit of measurement for the Time-series.
- **lower_bound:** A number indicating the lower limit of the Time-series' value range.
- **upper_bound:** A number indicating the upper limit of the Time-series' value range.
- **tags:** An array of strings used as tags for the Time-series.

For more details, please review our [OpenAPI specification](https://customer.noda.se/api/v2).


### Things

In the EnergyView APIv2, a "Thing" is a versatile object that serves as a container for grouping Time-series. It can represent any physical or conceptual entity, such as a radiator circuit, a heating system, or a pump station. This flexibility allows Things to be adapted to a wide range of applications.

- **Creation and Management:** Things can be created, updated, and deleted through the API. This includes setting names, types, and states and associating them with parent or child Things.
- **Associations:** Things are associated with Time-series and can have hierarchical relationships with other Things, represented by parent and child UUIDs.
- **Tagging and Categorization:** Things can be tagged for more accessible organization and retrieval.

The model of a Thing is as follows;

- **uuid:** A unique string identifier for the Thing, represented in UUID format.
- **name:** A string representing the Thing's name, with a minimum length requirement.
- **state:** A string indicating the current state of the Thing.
- **type:** A string specifying the type of the Thing, such as 'office/building', is optional.
- **created_by:** A string representing the UUID of the user who created the Thing.
- **tags:** An array of strings serving as identifying tags for the Thing.
- **parent:** A string representing the UUID of a parent Thing, if any.
- **children:** An array of strings, each representing the UUID of a child Thing.

For more details, please review our [OpenAPI specification](https://customer.noda.se/api/v2).

### Datasets

Datasets in EnergyView API v2 are complex data structures that allow storing and managing a wide range of data types. They are essential for situations where detailed and multifaceted data is necessary.

Key features of Datasets include:

- **UUID Identification:** A UUID uniquely identifies each Dataset.
- **Enhanced Data Storage:** Unlike Time-series, which handle simple time-value pairs, Datasets can store complex, structured data.
- **Flexible Data Types:** They support various data formats, accommodating diverse data storage needs.
- **Operational Capabilities:** The API facilitates the creation, updating, retrieval, and management of Datasets.
- **Integration with Things:** Datasets can be linked to specific Things for context and easier data management.

The model of a Dataset is as follows;

- **uuid:** The unique identifier for each Dataset, in UUID format.
- **name:** A human-readable name for the Dataset.
- **format:** Indicates the format of the stored content, such as CSV, JSON, XML, YAML.
- **size:** The size of the Dataset content in bytes.
- **checksum:** A SHA256 checksum of the content for integrity verification.
- **thing_uuid:** An optional reference to a Thing (Node/Thing), if applicable.
- **created:** Time-stamp for when the Dataset was created.
- **created_by:** Account ID of the user who created the Dataset.
- **updated:** Time-stamp for the last update of the Dataset.
- **updated_by:** Account ID of the user who last updated the Dataset.
- **tags:** Optional tags used for filtering and identification.

For more details, please review our [OpenAPI specification](https://customer.noda.se/api/v2).

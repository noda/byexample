---
priority: 10
---
# Common Tags/Sensors

[Back to index](/index.html)

This page lists the common tags/sensors that are available in the EnergyView system. The tags are grouped by their type.


## Tags available to "Kelp-Basic" devices

| Tag                                | Type        | Description                                                        | Unit             |
|------------------------------------|-------------|--------------------------------------------------------------------|------------------|
| `enco_indoortemp_average`          | Temperature | The average indoor temperature. As computed by the ENCO controller. | Celsius          |
| `enco_indoortemp_min`              | Temperature | The minimum indoor temperature. As computed by the ENCO controller. | Celsius          |
| `enco_limit_hi`                    | Temperature | The high limit of the indoor temperature. As set by the ENCO controller. | Celsius       |
| `enco_limit_lo`                    | Temperature | The low limit of the indoor temperature. As set by the ENCO controller. | Celsius        |
| `enco_outdoortemp_offset`          | Temperature | The offset that is applied to the outdoor temperature. As set by the ENCO controller. | Kelvin |
| `enco_target`                      | Temperature | The target temperature. As set by the ENCO controller.             | Celsius          |
| `meter_effect`                     | Power       | The power consumption of the building.                              | Kilowatt         |
| `meter_heatenergy`                 | Energy      | The heat energy consumption of the building.                        | Megawatt hour    |
| `meter_primreturntemp`             | Temperature | The primary return temperature.                                     | Celsius          |
| `meter_primsupplytemp`             | Temperature | The primary supply temperature.                                     | Celsius          |
| `meter_volume`                     | Volume      | The volume of the building.                                         | Cubic meter      |
| `meter_volumeflow`                 | Volume flow | The volume flow of the building.                                    | Liter per hour   |
| `operational_state`                | State       | The operational state of the algorithm.                             | Integer          |
| `outdoortemp`                      | Temperature | The outdoor temperature.                                            | Celsius          |
| `outdoortemp_fake`                 | Temperature | The outdoor temperature, but with the offset applied.               | Celsius          |
| `outdoortemp_offset`               | Temperature | The offset that is applied to the outdoor temperature.              | Kelvin           |
| `returntemp_sec`                   | Temperature | The secondary return temperature.                                   | Celsius          |
| `supplytemp_sec`                   | Temperature | The secondary supply temperature.                                   | Celsius          |
| `supplytemp_sec_controller_setvalue`| Temperature | The secondary supply temperature set value.                         | Celsius          |
| `supplytemp_sec_offset`            | Temperature | The offset that is applied to the secondary supply temperature.      | Kelvin           |
| `user_temporary_heat_shift`        | Temperature | The temporary heat shift. As set by the user.                        | Kelvin           |



## Tags available to "Generic Indoor Sensor" devices

| Tag | Type | Description | Unit |
| --- | --- | --- | --- |
| `indoortemp` | Temperature | The indoor temperature. | Celsius |
| `humidity` | Humidity | The indoor humidity. | Percent |
| `rssi` | Signal strength | The signal strength. | dBm |

# SensorFusion — Disaster Management

A Python model for describing, organizing, and assigning a large taxonomy of
sensors across different building types, aimed at disaster-management and
smart-building scenarios (collapse detection, gas/fire monitoring, person
tracking, post-earthquake search, and so on).

Buildings and sensors are modeled as objects, while a `SensorManager` keeps the
whole deployment as queryable **pandas** tables. Assignment is driven by a small
query language (one sensor per building, one per floor, etc.) that is gated by a
building/sensor **constraint matrix**.

> **Status:** early-stage / work-in-progress. The class taxonomy, manager, and
> query layer are functional; the constraint matrix and `database_manager.py`
> are still scaffolding (see [Roadmap](#roadmap)).

## Concept

The core idea is a "sensor fusion" catalog for disaster management:

- **Sensors** are organized into a deep inheritance hierarchy by purpose
  (disaster detection, smart-home monitoring, person tracking, after-earthquake
  search).
- **Buildings** of different kinds (apartment complex, hospital, school, …) host
  those sensors.
- A **manager** decides *which* sensors may be placed in *which* buildings and
  *how many* (per building, per floor, …), enforcing constraints, and records
  the result as flat tables suitable for analysis.

## Project structure

| File / package        | Responsibility                                                                                       |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| `sensor.py`           | `Sensor` base class and the full sensor taxonomy (categories and concrete sensor types).             |
| `building/`           | Building model: a base building plus the concrete building types that host sensors.                  |
| `sensor_manager.py`   | `SensorManager` — registers buildings/sensors, runs assignment queries, maintains pandas tables.      |
| `query_types.py`      | `SensorQuery` enum and the building↔sensor constraint matrix.                                         |
| `database_manager.py` | `DatabaseManager` — a broader persistence/registry layer (currently a stub).                          |
| `main.py`             | Entry point with a worked example (currently commented out).                                          |

## Requirements

- **Python 3.10+** (the manager uses `match`/`case` statements)
- **pandas**

```bash
pip install pandas
```

## How it works

### Sensors

Every sensor derives from `Sensor`, which carries common attributes:

`sid` (sensor id), `bid` (building id), `category`, `type`, `is_smart`,
`brand`, `model`, `speed`, `price`, and `success`.

`get_df()` returns a single-row `pandas.DataFrame` of the sensor's attributes,
which is how sensors get folded into the manager's tables.

The taxonomy is grouped into four top-level categories:

- **DisasterDetector**
  - `CollapseDetector` → `MotionCS`, `BeamCS`
  - `Seismic`
  - `Airborn` → `Drone`, `Satellite`, `Airplane`
- **SmartHomeDetector**
  - `WaterLeakageDetector`
  - `GasDetector` → `CarbonMonoxideDetector`, `SmokeDetector`
  - `MotionDetector`, `FireDetector`, `CameraSHD`
- **PersonTracker**
  - `GPS` → `GPSTracker`, `MobilePhoneTracker` → `AppTracker`, `BaseStationTracker`
  - `OpticalDetector` → `FaceRecognizer`, `PeopleCounter` → `CameraPC`, `BeamPC`
  - `SmartUtilityMeter` → `ElectricityUM`, `WaterUM`, `GasUM`
- **AfterEarthquake**
  - `MicrophoneDetector`, `CarbonDioxideDetector`, `MicrowaveRadar`

### Buildings

Buildings host sensors and expose a `floor_count`, a `sensor_list`, an `id`, a
`get_df()` method, and a `check_constraints()` method used by the manager. The
building types recognized by the constraint matrix are:

`ApartmentComplex`, `FireStation`, `Hospital`, `Mall`, `PoliceStation`,
`ReligiousBuildings`, and `School`.

### Assignment queries

`SensorQuery` defines how a sensor is rolled out across a building:

| Query                    | Meaning                                                  | Implemented |
| ------------------------ | -------------------------------------------------------- | :---------: |
| `AssignToBuilding`       | One sensor for the building                              | ✅ |
| `AssignToBuildingMulti`  | `value` sensors for the building                         | ✅ |
| `AssignToFloors`         | One sensor per floor                                     | ✅ |
| `AssignToFloorsMulti`    | `value` sensors per floor                                | ✅ |
| `AssignToApartments`     | Per-apartment placement                                  | planned |
| `AssignToApartmentsMulti`| `value` sensors per apartment                            | planned |

Each `sensor_query` first calls the target building's `check_constraints()` so
that only sensor/building/query combinations allowed by the constraint matrix
are applied. The manager deep-copies each placed sensor, assigns it a fresh
`sid`, links it to the building, and appends it to the `sensorDB` table.

## Usage

A minimal end-to-end example (this mirrors the demo in `main.py`):

```python
import sensor
import building
from sensor_manager import SensorManager
from query_types import SensorQuery

manager = SensorManager()

# Register buildings (each gets an auto-incremented id: 0, 1, ...)
b0 = building.ApartmentComplex()
b0.floor_count = 4
manager.add_building(b0)                            # building id 0
manager.add_building(building.ApartmentComplex())   # building id 1

# Create a sensor
co_detector = sensor.CarbonMonoxideDetector()

# Assign sensors via queries
manager.sensor_query(co_detector, 0, SensorQuery.AssignToFloors)    # one per floor of building 0
manager.sensor_query(co_detector, 1, SensorQuery.AssignToBuilding)  # one for building 1

# Inspect the resulting tables
print(manager.sensorDB)     # all placed sensors
print(manager.buildingDB)   # all registered buildings
```

Then run:

```bash
python main.py
```

## Roadmap

- Populate the building↔sensor **constraint matrix** with real rules (currently
  every sensor/building pair permits every query as a placeholder).
- Implement the apartment-level queries (`AssignToApartments`,
  `AssignToApartmentsMulti`).
- Flesh out `DatabaseManager` (floors, apartments, persons, sensor variations,
  base stations, air gadgets) into a full registry/persistence layer.
- Add tests and example datasets.

## License

No license has been specified yet. Until one is added, the default copyright
terms apply and reuse rights are reserved by the author.

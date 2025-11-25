# Data

The temporal extent of the datasets covers the period Apr - Oct 2025, split as follows:

- flights for Apr - Aug 2025: training dataset (3.1GiB)
- flights for Sep 2025: phase 1 submission / ranking
- flights for (maybe Sep and) Oct 2025: phase 2 submission / final ranking

The dataset for final ranking will be completely hidden to participating teams; we will only provide `fuel_final_submission.parquet` to be filled with the prediction of the relevant model.

## Fuel Burnt/Flown

We collected fuel information (via Open-Source Intelligence (OSINT)) for flights between April and September 2025.

Dataset:

1. `fuel_train.parquet`: for training
2. `fuel_rank_submission.parquet`: for submission ( `fuel_kg` values set to `0` \[zero\])
3. `fuel_final_submission.parquet`: for final ranking ( `fuel_kg` values set to `0` \[zero\])

The columns of the fuel flown/burnt dataset are ( `d_` stands for delta):

- `idx`: row id
- `flight_id`: a unique identifier of the flight in the flight list (note: each flight has on average 12 segments)
- `start`: a time instant ( [Coordinated Universal Time (UTC)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_UTC))
- `end`: a time instant ( [UTC](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_UTC))
- `fuel_kg`: fuel burnt between start and end

## Flight list [Anchor](https://ansperformance.eu/study/data-challenge/dc2025/data.html\#flight-list)

Dataset:

1. `flightlist_train.parquet`: for training
2. `flightlist_rank.parquet`: for ranking
3. `flightlist_final.parquet`: for ranking

The following is the list of columns in the flight list dataset:

- `flight_id`: a unique identifier for the flight
- `flight_date`: the date of the flight
- `takeoff`: the [UTC](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_UTC) timestamp of the take-off time
- `origin_icao`: the [International Civil Aviation Organization (ICAO)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ICAO) code of the [Aerodrome of DEParture (ADEP)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ADEP), the origin of the flight
- `origin_name`: the name of [ADEP](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ADEP)
- `landed`: the [UTC](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_UTC) timestamp of the landing time
- `destination_icao`: the [ICAO](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ICAO) code of the [Aerodrome of DEStination (ADES)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ADES), the destination of the flight
- `destination_name`: the name of [ADEP](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ADEP)
- `aircraft_type`: the [ICAO](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ICAO) aircraft type code of the aircraft carrying out the flight

## Trajectories [Anchor](https://ansperformance.eu/study/data-challenge/dc2025/data.html\#trajectories)

Dataset:

1. `flights_train/<flight_id>.parquet`: for training
2. `flights_rank/<flight_id>.parquet`: for rankining

We have trajectory files for each flight with fuel flow segments. These are (mainly) [Automatic Dependent Surveillance–Broadcast (ADS-B)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ADS_B) position reports for the flights in the flight list as available in OpenSky Network historical database. These flight trajectories are possibly incomplete, i.e. they can lack portions. We have augmented these trajectories with positional information coming from ACARS; the `source` column would categorize the origin of the data, either `adsb` or `acars`.

Each trajectory is described by (units in square brackets)

- `flight_id`: an identifier for the flight (details in the flight list dataset), i.e. `prc770822360`
- `timestamp`: timestamp for the position report \[UTC\]
- `longitude`: longitude in [Decimal degrees (DD)](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_DD) in \[-180, 180\] range
- `latitude`: latitude in [DD](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_DD) in \[-90, 90\] range
- `altitude`: altitude \[ft\]
- `groundspeed`: ground speed \[knots, kt\]
- `track`: track angle in [DD](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_DD)
- `vertical_rate`: vertical rate of climb/descent \[ft/min\]
- `mach`: the Mach number (from `source` = `acars`)
- `typecode`: the ICAO aircraft type, i.e. `A21N` for the Airbus A321neo
- `TAS`: **T** rue **A** ir **S** peed (from `source` = `acars`) \[kt\]
- `CAS`: **C** alibrated **A** ir **S** peed (from `source` = `acars`) \[kt\]
- `source`: the origin of the information; it can be `adsb` or `acars`

## Airports [Anchor](https://ansperformance.eu/study/data-challenge/dc2025/data.html\#airports)

Dataset: `apt.parquet`

The airports dataset provides complementary positions as follows:

- `icao`: the [ICAO](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_ICAO) code of the airport
- `longitude`: the airport longitude in [DD](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_DD) in \[-180, 180\] range
- `latitude`: the airport latitude in [DD](https://ansperformance.eu/study/data-challenge/dc2025/data.html#acronyms_DD) in \[-90, 90\] range
- `elevation`: the airport elevation \[ft\]

# List of Acronyms

**ADEP**: Aerodrome of DEParture

**ADES**: Aerodrome of DEStination

**ADS-B**: Automatic Dependent Surveillance–Broadcast

**DD**: Decimal degrees

**ICAO**: International Civil Aviation Organization

**UTC**: Coordinated Universal Time
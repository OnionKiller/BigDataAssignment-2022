# GTFS

## Chart
![Chart](assets/gtfs.png)

## Mapping
| Variable name              | Original table | Original name         |
|----------------------------|----------------|-----------------------|
| agency_name                | agency         | agency_name           |
| route_name                 | routes         | route_short_name      |
| route_type                 | routes         | route_type            |
| route_desc                 | routes         | route_desc            |
| trip_id                    | trips          | trip_id               |
| trip_direction             | trips          | direction_id          |
| trip_wheelchair_accessible | trips          | wheelchair_accessible |
| trip_bikes_allowed         | trips          | bikes_allowed         |
| trip_boarding_door         | trips          | boarding_door         |
| stop_arrival_time          | stop_times     | arrival_time          |
| stop_departure_time        | stop_times     | departure_time        |
| stop_id                    | stops          | stop_id               |
| stop_name                  | stops          | stop_name             |
| stop_latitude              | stops          | stop_lat              |
| stop_longitude             | stops          | stop_lon              |
| stop_location_type         | stops          | location_type         |
| stop_wheelchair_boarding   | stops          | wheelchair_boarding   |

## Dictionary

| Variable                  | Variable name              | Measurement unit | Allowed values                                                      | Description                                                            |
|---------------------------|----------------------------|------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| Agency name               | agency_name                | Text             |                                                                     | Full name of the transit agency.                                       |
| Route name                | route_name                 | Text             |                                                                     | Short name of a route.                                                 |
| Route type                | route_type                 | Numeric          | 0 - tram, 1 - metro, 3 - bus, 4 - ferry, 11 - trolleybus, 109 - hev | Indicates the type of transportation used on a route.                  |
| Route description         | route_desc                 | Text             |                                                                     | Description of the route                                               |
| Trip ID                   | trip_id                    | Text             |                                                                     | Identifies a trip.                                                     |
| Trip direction            | trip_direction             | Numeric          | 0 - normal, 1 - opposite                                            | Indicates the direction of travel for a trip.                          |
| Wheelchair accessible     | trip_wheelchair_accessible | Numeric          | 0 - unknown, 1 - yes, 2 - no                                        | Indicates wheelchair accessibility.                                    |
| Bikes allowed             | trip_bikes_allowed         | Numeric          | 0 - unknown, 1 - yes, 2 - no                                        | Indicates whether bikes are allowed.                                   |
| Boarding door             | trip_boarding_door         | Numeric          | 0 - any, 2 - front door only                                        | Indicates whether on which door can be board.                          |
| Arrival time              | stop_arrival_time          | HH:MM:SS         |                                                                     | Arrival time at a specific stop for a specific trip on a route.        |
| Departure time            | stop_departure_time        | HH:MM:SS         |                                                                     | Departure time from a specific stop for a specific trip on a route.    |
| Stop ID                   | stop_id                    | Text             |                                                                     | Identifies a stop, station, or station entrance.                       |
| Stop name                 | stop_name                  | Text             |                                                                     | Name of the location.                                                  |
| Stop location (latitude)  | stop_latitude              | Numeric          | -90 - +90                                                           | Latitude of the location.                                              |
| Stop location (longitude) | stop_longitude             | Numeric          | -180 - +180                                                         | Longitude of the location.                                             |
| Stop location type        | stop_location_type         | Numeric          | 0 - stop, 1 - station, 2 - entrance/exit                            | Type of the location                                                   |
| Wheelchair boarding       | stop_wheelchair_boarding   | Numeric          | 0 - unknown, 1 - yes, 2 - no                                        | Indicates whether wheelchair boardings are possible from the location. |


| V??ltoz??                    | V??ltoz?? neve               | T??pus    | Megengedett ??rt??kek                                                 | Le??r??s                                                                |
|----------------------------|----------------------------|----------|---------------------------------------------------------------------|-----------------------------------------------------------------------|
| Szolg??ltat?? neve           | agency_name                | Sz??veges |                                                                     | A szolg??ltat?? teljes neve.                                            |
| J??rat neve                 | route_name                 | Sz??veges |                                                                     | Az j??rat r??vid neve.                                                  |
| J??rat t??pusa               | route_type                 | Sz??m     | 0 - villamos, 1 - metr??, 2 - busz, 3 - haj??, 4 - trolibusz, 5 - h??v | A j??ratot kiszolg??l?? j??rm?? t??pusa.                                    |
| J??rat le??r??sa              | route_desc                 | Sz??veges |                                                                     | A j??rat r??vid le??r??sa.                                                |
| ??tvonal azonos??t??ja        | trip_id                    | Sz??veges |                                                                     | K??t meg??ll?? k??z??tti utaz??s azonos??t??ja.                               |
| ??tvonal ir??nya             | trip_direction             | Sz??m     | 0 - norm??l, 1 - ellent??tes                                          | Az utaz??s menetir??ny??t jelzi.                                         |
| Kerekessz??kkel el??rhet??    | trip_wheelchair_accessible | Sz??m     | 0 - ismeretlen, 1 - igen, 2 - nem                                   | Azt jelzi, hogy a j??raton kerekessz??kkel lehets??ges-e utazni.         |
| Ker??kp??rok enged??lyezettek | trip_bikes_allowed         | Sz??m     | 0 - ismeretlen, 1 - igen, 2 - nem                                   | Azt jelzi, hogy megengedett-e a ker??kp??r sz??ll??t??s.                   |
| Besz??ll?? ajt??              | trip_boarding_door         | Sz??m     | 0 - b??rmelyik, 1 - els?? ajt??                                        | Azt jelzi, hogy melyik ajt??n lehet-e felsz??llni.                      |
| ??rkez??si id??               | stop_arrival_time          | HH:MM:SS |                                                                     | ??rkez??si id?? egy adott meg??ll??helyen egy adott utaz??shoz.             |
| Indul??si id??               | stop_departure_time        | HH:MM:SS |                                                                     | Indul??si id?? egy adott meg??ll??b??l egy adott utaz??shoz.                |
| Meg??ll?? azonos??t??ja        | stop_id                    | Sz??veges |                                                                     | Meg??ll??helyet, ??llom??st vagy ??llom??s bej??rat??t azonos??tja.            |
| Meg??ll?? neve               | stop_name                  | Sz??veges |                                                                     | A meg??ll?? neve.                                                       |
| Meg??ll?? helye (sz??less??g)  | stop_latitude              | Sz??m     | -90 - +90                                                           | A meg??ll?? koordin??t??j??nak sz??less??gi foka.                            |
| Meg??ll?? helye (hossz??s??g)  | stop_longitude             | Sz??m     | -180 - +180                                                         | A meg??ll?? kordin??t??j??nak hossz??s??gi foka.                             |
| Meg??ll?? t??pusa             | stop_location_type         | Sz??m     | 0 - meg??ll??, 1 - ??llom??s, 2 - ??llom??s bej??rat/kij??rat               | A meg??ll?? t??pusa.                                                     |
| Kerekessz??kes besz??ll??s    | stop_wheelchair_boarding   | Sz??m     | 0 - ismeretlen, 1 - igen, 2 - nem                                   | Azt jelzi, hogy a meg??ll??b??l lehets??ges-e a kerekessz??kes felsz??ll??s. |

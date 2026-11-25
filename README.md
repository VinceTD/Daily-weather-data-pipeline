# Weather Data Pipeline

## Purpose
This data will be relevant to people interested in moving to or touring Chicago.
Historical data will contextualize current weather conditions.

## Data source
I will use Open-Meteo to collect hourly temperature and precipitation
forecasts for Chicago, including timestamps and measurement units.

Version 1 will collect forecasts. A future extension will add historical
weather data to help contextualize forecast conditions.

## Planned pipeline
Request data → validate and clean → load into PostgreSQL → log results.

## Definition of done
- A Python command retrieves weather forecasts for Chicago.
- Records are validated before loading into PostgreSQL.
- Missing or invalid values are handled explicitly and logged.
- Running the pipeline twice with the same input creates no duplicate records.
- The pipeline runs daily without manual intervention.
- Each run logs its outcome and the number of records processed.
- A deliberately failed run triggers a notification.
- The README explains how to install, configure, and run the project.

## Project status
The repository and initial project scope are complete.
Pipeline implementation has not started.

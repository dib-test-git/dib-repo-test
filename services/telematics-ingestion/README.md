# Telematics Ingestion

Pulls machine telemetry (SMU hours, location, fuel, fault codes) from the Cat Link API into Al-Bahar's data warehouse. Tracked by issue #9.

## Responsibilities

- Poll Cat Link REST endpoints per asset
- Push fault-code and geofence events to the event bus within 5 minutes
- Deduplicate machines across country databases (ERP asset ID join)
- Emit an alert when a machine stops reporting for > 24 hours

## Configuration

| Variable | Description |
|---|---|
| `CATLINK_CLIENT_ID` | Issued by the Caterpillar partner team |
| `CATLINK_CLIENT_SECRET` | OAuth client secret (vaulted) |
| `WAREHOUSE_DSN` | Destination warehouse connection string |
| `EVENT_BUS_URL` | Internal event bus endpoint |

## Known gaps

Only ~60% of the active rental fleet is Cat Link-capable. Older machines fall through to the manual process until the retrofit program lands.

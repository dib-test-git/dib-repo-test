"""Thin wrapper around the Cat Link REST API."""

from __future__ import annotations

import time
from dataclasses import dataclass


@dataclass
class TelemetrySnapshot:
    asset_id: str
    smu_hours: float
    fuel_level_pct: float
    latitude: float
    longitude: float
    fault_codes: list[str]
    observed_at: float


class CatLinkClient:
    """Polls Cat Link for telemetry. Real implementation uses OAuth2 + retries."""

    def __init__(self, client_id: str, client_secret: str, base_url: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url.rstrip("/")

    def fetch_latest(self, asset_id: str) -> TelemetrySnapshot:
        # TODO(#9): replace with real HTTP call once partner credentials are issued.
        return TelemetrySnapshot(
            asset_id=asset_id,
            smu_hours=0.0,
            fuel_level_pct=0.0,
            latitude=0.0,
            longitude=0.0,
            fault_codes=[],
            observed_at=time.time(),
        )

"""Map Cat Link asset IDs to canonical ERP asset IDs across the 5 countries."""

from __future__ import annotations

from collections.abc import Mapping


def resolve_erp_asset_id(
    catlink_asset_id: str,
    country: str,
    lookup: Mapping[tuple[str, str], str],
) -> str | None:
    """Return the canonical ERP asset ID, or None if unmapped."""
    return lookup.get((country.upper(), catlink_asset_id))

from services.telematics_ingestion.src.dedupe import resolve_erp_asset_id


def test_resolves_known_asset() -> None:
    lookup = {("UAE", "CL-123"): "ERP-AE-00042"}
    assert resolve_erp_asset_id("CL-123", "uae", lookup) == "ERP-AE-00042"


def test_returns_none_for_unknown() -> None:
    assert resolve_erp_asset_id("CL-999", "UAE", {}) is None

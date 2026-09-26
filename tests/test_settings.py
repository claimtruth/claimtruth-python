from pathlib import Path

import pytest

from claimtruth.settings import Settings


@pytest.fixture(autouse=True)
def isolated_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    # Keep a developer's local .env and CLAIMTRUTH_* variables out of these tests.
    monkeypatch.chdir(tmp_path)
    for name in ("CLAIMTRUTH_CONTACT_EMAIL", "CLAIMTRUTH_DATA_DIR", "CLAIMTRUTH_MODEL_ALIASES"):
        monkeypatch.delenv(name, raising=False)


def test_defaults() -> None:
    settings = Settings()

    assert settings.contact_email is None
    assert settings.data_dir == Path(".cache")
    assert settings.model_aliases == {}


def test_reads_prefixed_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CLAIMTRUTH_CONTACT_EMAIL", "maintainers@example.org")
    monkeypatch.setenv("CLAIMTRUTH_DATA_DIR", "/tmp/claimtruth-data")

    settings = Settings()

    assert settings.contact_email == "maintainers@example.org"
    assert settings.data_dir == Path("/tmp/claimtruth-data")


def test_model_aliases_parse_from_json_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(
        "CLAIMTRUTH_MODEL_ALIASES",
        '{"judge": {"model_id": "example-model", "family": "example", "max_tokens": 1024}}',
    )

    settings = Settings()

    assert settings.model_aliases["judge"].family == "example"
    assert settings.model_aliases["judge"].max_tokens == 1024

from typer.testing import CliRunner

from claimtruth import __version__
from claimtruth.cli import app

runner = CliRunner()


def test_version_prints_installed_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.stdout.strip() == f"claimtruth {__version__}"

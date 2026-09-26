"""The `claimtruth` command-line interface."""

import typer

from claimtruth import __version__

app = typer.Typer(no_args_is_help=True, help="ClaimTruth: verify claims against their sources.")


@app.callback()
def main() -> None:
    """ClaimTruth: verify claims against their sources."""


@app.command()
def version() -> None:
    """Print the installed ClaimTruth version."""
    typer.echo(f"claimtruth {__version__}")

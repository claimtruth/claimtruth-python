# ClaimTruth

ClaimTruth checks whether a cited source actually supports a claim **at the claim's stated scope and strength**. For every claim it returns a typed, evidence-linked verdict (`supported`, `overstated`, `contradicted`, `not_in_source`, ...) whose evidence points at exact character offsets in a hashed copy of the source, or it abstains with a reason when it can't tell. It is open source under Apache-2.0 and built in public.

**Status:** pre-alpha. Nothing here is ready for real use yet.

## Install

Requires [uv](https://docs.astral.sh/uv/) (it fetches Python 3.12 for you).

```bash
git clone https://github.com/claimtruth/claimtruth-python.git
cd claimtruth-python
uv sync
uv run claimtruth version
```

Configuration comes from environment variables prefixed with `CLAIMTRUTH_`; see `.env.example` for the names.

## Development

```bash
uv run ruff check . && uv run ruff format --check .
uv run pyright
uv run pytest -q
```

## License

Apache-2.0. See [LICENSE](LICENSE).

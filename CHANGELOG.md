# Changelog

All notable changes to this project are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Repository bootstrap: uv-managed Python 3.12 package with a src layout, ruff, pyright
  (strict on `src/`), pytest, pre-commit and GitHub Actions CI.
- `claimtruth version` CLI command.
- `claimtruth.settings` with the `CLAIMTRUTH_` env prefix (`CONTACT_EMAIL`, `DATA_DIR`,
  `MODEL_ALIASES`).

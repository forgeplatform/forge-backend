# Changelog

All notable changes to the Forge Backend will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project adheres to CalVer (`YYYY.MM.PATCH`).

## [Unreleased]

## [2026.04.0] - 2026-04-17

### Added
- Multi-Tenancy v2: per-tenant Celery queue routing and per-tenant
  API rate limiting (token bucket via Redis)
- Recommendations engine with 12 rules and REST API
- Standalone tests separated from the AWX-inherited test suite
- Podman installed in the runtime image for EE container isolation
- `23-recommendations` API reference doc
- Assistant API surface for the Ollama+RAG chat sidecar

### Changed
- Renamed all `awx-*` references to `forge-*` in user-facing strings,
  CLI commands (`forge-manage`), Django app labels, and docs
- Cleaned up legacy AWX docs and updated README links

### Fixed
- psycopg 3.2 API break in `PubSub.current_notifies`
- Migration ordering for fresh installs against existing AWX databases

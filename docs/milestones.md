# Milestones & Roadmap

## Milestone 0 — Repo scaffolding
- Create repo structure, base README, architecture docs, and sample SVG diagram.
- Add initial requirements and simple starter files for each component.

## Milestone 1 — Simulator v0
- Implement scenario runner
- Provide 3 sample scenarios (lateral_movement, data_exfil, phishing_click)
- CLI flags: --scenario, --sink, --speed

## Milestone 2 — Normalizer + Sigma-lite v0
- FastAPI /ingest endpoint
- Canonical normalization
- In-memory rule engine with 3 rules and alert endpoint

## Milestone 3 — Deception v0
- HTTP honeypot + simple honeytoken generator
- Integration to send hits to normalizer

## Milestone 4 — UI v0
- Single-file dark-themed HTML/JS UI with live event stream, controls, and alerts pane

## Milestone 5 — Polish
- Tests, CI, Docker-Compose, demo GIF, README polish

Estimated total MVP time: ~2 weeks of focused work

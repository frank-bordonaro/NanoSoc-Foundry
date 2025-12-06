# Architecture notes

- Simulator produces JSON events; sink options: HTTP POST to /ingest, write to disk (JSONL), or publish to message bus.
- Normalizer receives events and converts to canonical schema; it also runs Sigma-lite rules against a sliding window in memory and emits alerts (POST /alerts or writes to disk).
- Deception services generate events when honeytokens/honeypots are touched and send them to the normalizer.
- UI connects to normalizer via SSE/WebSocket for live stream and can request actions (start/stop scenarios) from orchestrator.
- Orchestrator is an optional convenience script to launch and wire the components.

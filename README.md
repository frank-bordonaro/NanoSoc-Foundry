# NanoSOC Foundry — Small SOC Suite Starter Kit

**Tagline:** Tiny tools, massive insight — a modular Small-SOC simulator, normalizer, and deception toolkit you can run locally and extend.

## Overview
NanoSOC Foundry is a ready-to-run starter kit for building a vendor-neutral Small SOC playground. It's designed for security engineers, detection engineers, and sales engineers who want a portable demo environment: generate synthetic alerts, normalize and correlate logs with Sigma-like rules, deploy lightweight deception artifacts such as honeytokens and canaries, and visualize live events in a sleek web UI.

This kit is purposely modular and approachable — everything runs locally and can be extended to push to Elasticsearch, MISP, or a real SIEM. 

---
## Contents of this ZIP
- `architecture/` — diagrams (SVG) and styled visual notes describing the architecture.
- `simulator/` — scenario-based event generator that sinks JSON events to the normalizer.
- `normalizer/` — FastAPI-based ingestion and Sigma-lite correlator.
- `deception/` — tiny honeypot + honeytoken & canary generator service with AKIA-style tokens.
- `ui/` — single-file HTML/JS UI for live event streaming and alert visualization.
- `orchestrator/` — startup script to run components locally for demos.
- `docs/` — milestones, microtasks, roadmap, example scenarios, and demo instructions.
- `requirements.txt` — top-level Python dependencies for the MVP.

---
## Quickstart (unzip & run demo)
Assuming Python 3.10+ and Unix-like shell:
```bash
unzip NanoSOC_Foundry.zip -d ./
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start normalizer
python normalizer/app.py &

# Start deception service
python deception/deception_service.py &

# Start UI (open in browser)
open ui/index.html

# Run simulator scenario (example)
python simulator/simulator.py --scenario simulator/scenarios/lateral_movement.json --sink http://localhost:8001/ingest --speed 2.0
```

This kit intentionally favors minimal external tooling; however a Docker Compose is included for convenience if you prefer containerized runs.

---
## Features & Workflows
- **Simulated Scenarios:** Lateral movement, process creation, authentication events.
- **Honeytokens & Canaries:** Generate AKIA-style honeytokens or canaries; logs alert if accessed.
- **Live Event Streaming:** Scrollable UI with color-coded alerts, timestamps, and event metadata.
- **Rule Engine:** Sigma-lite rules for detecting suspicious patterns, correlated across scenarios.
- **Extendable:** Add new scenarios, rules, or enrichments (GeoIP, etc.) easily.
- **Demo-Ready:** Perfect for internal demos, portfolio showcases, or SE/SOC training.


<!--
---
## Using Cline with NanoSOC Foundry
1. Point Cline at this repo root. Use the provided `cline_prompt.txt` as the persistent agent prompt.
2. Feed microtasks from `docs/microtasks.md` one at a time.
3. Run unit tests and scenario demos after each task to validate changes.

---
-->  
<br>
<br>  

## License
none

---
## Contact / Credits
Created for demonstration and portfolio use ONLY.

Generated: 2025-12-05T04:36:33.341402Z
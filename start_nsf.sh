#!/bin/bash
# NanoSOC Foundry demo starter
# Make sure this is run from project root

# Activate venv
source .venv/bin/activate

echo "Starting NanoSOC Foundry services..."

mkdir -p logs

# Start Normalizer API
.venv/bin/python -m nsf_normalizer.app > logs/normalizer.log 2>&1 &
echo "nsf_normalizer.app started on port 8001."

# Start Deception Service
.venv/bin/python -m deception.deception_service > logs/deception.log 2>&1 &
echo "deception_service started on port 9000."

# Start Honeytoken Service (already part of deception_service.py)
# port 9001
.venv/bin/python -m deception.deception_service > logs/honeytoken.log 2>&1 &
echo "Honeytoken service started on port 9001."

# Start Simulator API
.venv/bin/uvicorn simulator.api:app --host 127.0.0.1 --port 8002 --reload > logs/simulator_api.log 2>&1 &
echo "Simulator API started on port 8002."

# Start Web UI
.venv/bin/python -m http.server --directory ui 8000 > logs/ui.log 2>&1 &
echo "Web UI server started at http://localhost:8000."

echo "All services started. Check logs/ directory for output."
echo "Use Ctrl+C to stop all manually, or run 'pkill -f uvicorn' to kill APIs."

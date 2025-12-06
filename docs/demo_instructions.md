# Demo Instructions

1. Create and activate a virtualenv
2. pip install -r requirements.txt
3. Start normalizer: `python normalizer/app.py &`
4. Start deception: `python deception/deception_service.py &`
5. Open `ui/index.html` in your browser (File -> Open) OR run a simple HTTP server:
   `python -m http.server --directory ui 8000` then open http://localhost:8000
6. Run a scenario:
   `python simulator/simulator.py --scenario simulator/scenarios/lateral_movement.json --sink http://localhost:8001/ingest --speed 2.0`
7. Observe events printed in the normalizer console and in the UI.

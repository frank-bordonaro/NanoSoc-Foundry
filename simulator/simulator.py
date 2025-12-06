import argparse
import json
import time
import requests
from pathlib import Path

def load_scenario(path):
    with open(path, 'r') as f:
        return json.load(f)


def run_scenario(scenario_path, sink=None, speed=1.0):
    scenario = load_scenario(scenario_path)
    for event in scenario.get("events", []):
        payload = {"raw": event}
        try:
            if sink:
                # push to API if sink provided
                import requests
                requests.post(sink, json=payload, timeout=2)
        except Exception as e:
            print("Failed to send event", e)
        time.sleep(event.get("delay", 1.0) * (1.0 / speed))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scenario', required=True)
    parser.add_argument('--sink', default='http://localhost:8001/ingest')
    parser.add_argument('--speed', type=float, default=1.0)
    args = parser.parse_args()
    run_scenario(args.scenario, sink=args.sink, speed=args.speed)

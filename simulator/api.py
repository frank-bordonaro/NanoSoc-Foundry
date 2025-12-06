# simulator/api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import time
import threading
from simulator.simulator import run_scenario
import random
import string

app = FastAPI()

# Allow requests from UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

EVENTS_FILE = "ui/events.json"
EVENTS = []

scenario_running = False  # NEW — prevents duplicate logs
LEVEL_COLORS = {
    "info": "\033[94m",
    "alert": "\033[93m",
    "error": "\033[91m",
    "end": "\033[0m",
}

def append_event(event, level="info", event_type=None):
    """Append an event, save last 50, and colorize terminal output."""
    colored = f"{LEVEL_COLORS.get(level,'')}{event}{LEVEL_COLORS['end']}"
    print(colored)

    EVENTS.append({
        "timestamp": time.time(),
        "message": event,
        "level": level,
        "event_type": event_type,   # <— NEW
    })
    with open(EVENTS_FILE, "w") as f:
        json.dump(EVENTS[-50:], f)


@app.get("/run_scenario")
def trigger_scenario(name: str):
    """Run a scenario only once until it finishes."""
    global scenario_running

    if scenario_running:
        return {"status": "busy", "detail": "Scenario already running"}

    scenario_running = True

    scenario_path = f"simulator/scenarios/{name}.json"

    def run_in_thread():
        global scenario_running
        append_event(f"Starting scenario '{name}'",
                     "info",
                     event_type="scenario_status")

        run_scenario(
            scenario_path,
            sink="http://localhost:8002/push_event",
            speed=1.0
        )

        append_event(f"Scenario '{name}' finished.",
                     "info",
                     event_type="scenario_status")

        scenario_running = False

    threading.Thread(target=run_in_thread, daemon=True).start()
    return {"status": "started", "scenario": name}


@app.post("/push_event")
def push_event(event: dict):
    """Push events from simulator → UI."""
    global scenario_running

    # Ignore simulator output if scenario has already ended
    if not scenario_running:
        return {"status": "discarded", "reason": "scenario finished"}

    msg = event.get("raw", str(event))
    level = event.get("level", "info")

    append_event(msg, level, event_type=event.get("event_type"))
    return {"status": "ok"}


@app.get("/events.json")
def get_events():
    return EVENTS

@app.get("/create_honeytoken")
def create_honeytoken():
    """Generate a realistic AWS-style honeytoken and push it into the event stream."""

    # Generate 16 uppercase alphanumeric characters
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    # Full fake AWS access key
    token = f"AKIA{suffix}"

    append_event(
        f"Honeytoken created: {token}",
        level="alert",
        event_type="honeytoken"
    )

    return {"token": token}

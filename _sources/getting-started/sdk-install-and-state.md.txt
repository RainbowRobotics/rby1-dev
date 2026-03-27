# SDK Installation and Read State

Purpose: install the Python SDK and print a small piece of robot state.

## Install (Python)
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -U pip
pip install rby1-sdk
```

## Quick connectivity (example)
Replace host/port as appropriate.
```python
import rby1_sdk as rby

# Example endpoint:
endpoint = "192.168.12.1:50051"
model    = "a"

robot = rby.create_robot(endpoint, model)
robot.connect()

# Info
info = robot.get_robot_info()
print("Robot info:", info)

# State (basic)
state = robot.get_state()          # TODO: confirm available fields for your build
print("time:", getattr(state, "time", None),
      "mode:", getattr(state, "mode", None))
```

Further reading: see the SDK repository’s Python example `examples/python/03_robot_state.py` for a more complete state printout.

<!-- ## TODO
- [ ] Confirm default gRPC port
- [ ] Document required model key(s)
- [ ] List common state fields (time, mode, battery, joints, etc.) -->

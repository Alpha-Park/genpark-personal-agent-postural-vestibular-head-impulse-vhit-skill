# Video Head Impulse Test (vHIT) & Vestibular Gain Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of video Head Impulse Test (vHIT) angular vestibulo-ocular reflex (VOR) gain, overt/covert saccade quantification, and gaze stability.

```mermaid
flowchart TD
    HeadMotion["High-Frequency Angular Head Impulse (>150 deg/s)"] --> OpticalPupil["Pupil & Eye Compensatory Slow Phase"]
    OpticalPupil --> VOR_Math["VOR Gain Calculation (Eye Vel / Head Vel)"]
    VOR_Math --> SaccadeAudit["Catch-Up Saccade Area & Gaze Stability Engine"]
    SaccadeAudit --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Neuro-Otology Standards**: Implements validated algorithms for high-frequency angular canal excitation.
- **Dynamic Visual Acuity & Motion Sickness Stratification**: Direct quantification of retinal slip and vestibular compensation.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import VestibularHeadImpulseClient

client = VestibularHeadImpulseClient()
result = client.evaluate_vhit(
    head_velocity_deg_s=195.0,
    eye_velocity_deg_s=188.0,
    overt_saccades_count=0
)
print("VOR Gain:", result["vor_gain"])
print("Classification:", result["classification"])
```

## License
Apache-2.0

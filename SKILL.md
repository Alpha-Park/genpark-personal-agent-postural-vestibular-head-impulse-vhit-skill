---
name: genpark-personal-agent-postural-vestibular-head-impulse-vhit-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating video head impulse test (vHIT) high-frequency VOR gain, overt/covert catch-up saccades, and gaze stability.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Video Head Impulse Test (vHIT) & Vestibular Gain Skill

A sovereign personal agent capability for evaluating high-frequency angular vestibulo-ocular reflex (VOR) performance across individual semicircular canals, detecting corrective catch-up saccades, and optimizing gaze stabilization.

## Core Capabilities
- **High-Frequency VOR Gain**: Measures eye/head velocity ratio during rapid, passive angular impulses.
- **Saccade Quantification**: Distinguishes between overt (post-head movement) and covert (intra-head movement) saccades.
- **Vestibular Stability Score**: 0-100 rating indicating spatial motion orientation and simulator sickness resilience.
- **Vestibular Ergonomics**: Proactive gaze stabilization conditioning (VOR x1) and motion recovery drills.

## Fast Invocation
```python
from client import VestibularHeadImpulseClient

client = VestibularHeadImpulseClient()
res = client.evaluate_vhit(
    head_velocity_deg_s=195.0,
    eye_velocity_deg_s=188.0,
    overt_saccades_count=0,
    covert_saccades_count=0
)
print("VOR Gain:", res["vor_gain"])
print("Vestibular Score:", res["vestibular_stability_score"])
```

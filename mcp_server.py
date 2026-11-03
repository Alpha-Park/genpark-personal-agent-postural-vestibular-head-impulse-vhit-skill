"""
MCP Server for Video Head Impulse Test (vHIT) & Vestibular Gain Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating angular VOR gain and corrective catch-up saccades.
"""

import sys
import json
from typing import Dict, Any
from client import VestibularHeadImpulseClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_vhit",
                "description": "Calculates video Head Impulse Test (vHIT) high-frequency VOR gain, overt/covert saccades, and gaze stability score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "head_velocity_deg_s": {
                            "type": "number",
                            "description": "Peak angular velocity of passive head impulse in deg/s (e.g. 180.0 deg/s)."
                        },
                        "eye_velocity_deg_s": {
                            "type": "number",
                            "description": "Peak compensatory slow-phase eye velocity in deg/s (e.g. 172.0 deg/s)."
                        },
                        "overt_saccades_count": {
                            "type": "integer",
                            "description": "Number of post-impulse corrective saccades (e.g. 0).",
                            "default": 0
                        },
                        "covert_saccades_count": {
                            "type": "integer",
                            "description": "Number of intra-impulse covert corrective saccades (e.g. 0).",
                            "default": 0
                        },
                        "target_canal": {
                            "type": "string",
                            "description": "Semicircular canal tested (HORIZONTAL, ANTERIOR, POSTERIOR).",
                            "default": "HORIZONTAL"
                        }
                    },
                    "required": ["head_velocity_deg_s", "eye_velocity_deg_s"]
                }
            }
        ]
    }


def handle_request(client: VestibularHeadImpulseClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_vhit":
            res = client.evaluate_vhit(
                head_velocity_deg_s=float(args.get("head_velocity_deg_s", 180.0)),
                eye_velocity_deg_s=float(args.get("eye_velocity_deg_s", 172.0)),
                overt_saccades_count=int(args.get("overt_saccades_count", 0)),
                covert_saccades_count=int(args.get("covert_saccades_count", 0)),
                target_canal=str(args.get("target_canal", "HORIZONTAL"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = VestibularHeadImpulseClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()

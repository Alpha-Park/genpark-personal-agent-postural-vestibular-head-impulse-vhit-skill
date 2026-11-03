"""
Example Usage: Video Head Impulse Test (vHIT) & Semicircular Canal VOR Gain.
Demonstrates high-frequency gaze stabilization analysis and catch-up saccade detection.
"""

from client import VestibularHeadImpulseClient


def main():
    client = VestibularHeadImpulseClient()
    print("=== Video Head Impulse Test (vHIT) Dynamics Demo ===")

    # Test Case 1: Healthy normal VOR gaze stability (Right horizontal canal)
    res1 = client.evaluate_vhit(
        head_velocity_deg_s=195.0,
        eye_velocity_deg_s=188.0,
        overt_saccades_count=0,
        covert_saccades_count=0,
        target_canal="HORIZONTAL"
    )
    print("\nTest Case 1: Healthy Vestibular Response (Horizontal Canal)")
    print(f"  Head Velocity: {res1['head_velocity_deg_s']} deg/s | Eye Velocity: {res1['eye_velocity_deg_s']} deg/s")
    print(f"  VOR Gain: {res1['vor_gain']}")
    print(f"  Catch-up Saccades: {res1['total_catchup_saccades']}")
    print(f"  Vestibular Stability Score: {res1['vestibular_stability_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Vestibular hypofunction with overt catch-up saccades
    res2 = client.evaluate_vhit(
        head_velocity_deg_s=180.0,
        eye_velocity_deg_s=108.0,
        overt_saccades_count=2,
        covert_saccades_count=1,
        target_canal="HORIZONTAL"
    )
    print("\nTest Case 2: Vestibular Deficit with Catch-up Saccades")
    print(f"  VOR Gain: {res2['vor_gain']}")
    print(f"  Total Saccades: {res2['total_catchup_saccades']}")
    print(f"  Vestibular Score: {res2['vestibular_stability_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()

"""
Video Head Impulse Test (vHIT) & Semicircular Canal VOR Gain Engine.
Provides deterministic, zero-dependency modeling of high-frequency angular vestibulo-ocular reflex (VOR),
overt/covert corrective catch-up saccade quantification, and dynamic gaze stabilization kinetics.
"""

from typing import Dict, Any, List, Optional


class VestibularHeadImpulseClient:
    """
    Deterministic client for calculating video Head Impulse Test (vHIT) metrics.
    Assesses high-frequency semicircular canal VOR gain and corrective saccade dynamics
    to evaluate vestibular health, spatial disorientation, and motion sickness resilience.
    """

    def __init__(self):
        pass

    def evaluate_vhit(
        self,
        head_velocity_deg_s: float,
        eye_velocity_deg_s: float,
        overt_saccades_count: int = 0,
        covert_saccades_count: int = 0,
        target_canal: str = "HORIZONTAL"
    ) -> Dict[str, Any]:
        """
        Calculates vHIT VOR gain = Eye Velocity / Head Velocity.
        Normative reference:
        - Horizontal canals: 0.82 - 1.12
        - Vertical canals (Anterior/Posterior): 0.74 - 1.05
        """
        if head_velocity_deg_s <= 0 or eye_velocity_deg_s < 0:
            return {"error": "Head velocity must be positive and eye velocity non-negative"}

        gain = round(eye_velocity_deg_s / head_velocity_deg_s, 2)
        total_saccades = int(overt_saccades_count + covert_saccades_count)

        canal_type = target_canal.upper()
        lower_threshold = 0.82 if canal_type == "HORIZONTAL" else 0.74

        # Vestibular Gaze Stability Score (0 - 100):
        # Gain 0.90 - 1.05 with 0 saccades -> 90 - 100
        score = 80.0
        if 0.88 <= gain <= 1.08:
            score += 15.0
        elif gain >= lower_threshold:
            score += 5.0
        elif gain < 0.65:
            score -= 35.0
        elif gain < lower_threshold:
            score -= 20.0

        # Penalize for catch-up saccades (each indicates retinal slip compensation)
        score -= min(35.0, total_saccades * 12.0)

        stability_score = round(min(100.0, max(5.0, score)), 1)

        has_retinal_slip = gain < lower_threshold or total_saccades > 0

        if stability_score >= 85.0:
            tier = "OPTIMAL_VESTIBULO_OCULAR_STABILITY"
            interp = f"Near-unity VOR gain ({gain}) on {canal_type} canal with zero catch-up saccades; crisp dynamic gaze fixation."
            guidance = "Superior gaze stabilization during rapid head motion. High resilience to simulator and motion sickness."
        elif stability_score >= 70.0:
            tier = "NORMAL_DYNAMIC_VISUAL_ACUITY"
            interp = f"Preserved high-frequency VOR response ({gain}) on {canal_type} canal; physiological compensation intact."
            guidance = "Standard vestibular performance. Maintain normal postural exercise routines."
        elif not has_retinal_slip:
            tier = "MILD_CANAL_ASYMMETRY"
            interp = f"Borderline VOR gain ({gain}) on {canal_type} canal; mild sensory asymmetry."
            guidance = "Incorporate VOR x1 visual gaze stabilization drills (tracking visual target while rotating head)."
        else:
            tier = "VESTIBULAR_HYPOFUNCTION_GAZE_SLIP"
            interp = f"Deficient VOR gain ({gain} < {lower_threshold}) accompanied by {total_saccades} corrective catch-up saccades; significant retinal image slip."
            guidance = "Peripheral vestibular hypofunction detected. Limit rapid rotational tasks and consult neuro-otology or vestibular physical therapy."

        return {
            "target_canal": canal_type,
            "head_velocity_deg_s": head_velocity_deg_s,
            "eye_velocity_deg_s": eye_velocity_deg_s,
            "vor_gain": gain,
            "overt_saccades_count": overt_saccades_count,
            "covert_saccades_count": covert_saccades_count,
            "total_catchup_saccades": total_saccades,
            "vestibular_stability_score": stability_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }

# archetypal_narrative_mcp/server.py

from mcp.server.fastmcp import FastMCP
from typing import Literal, Optional, List, Dict
import json

mcp = FastMCP("archetypal-narrative")

# ============================================================================
# LAYER 1: PURE TAXONOMY (0 tokens)
# ============================================================================

ARCHETYPAL_ARCS = {
    "tragedy": {
        "description": "Freytag's pyramid: stability → hubris → catastrophe → recognition → diminishment",
        "sequence_length": 5,
        "canonical_form": "inverted_U_with_descent",
        "h1_requirement": "must_have_climax_and_denouement"
    },
    "comedy": {
        "description": "U-shaped: stability → disruption → crisis → reversal → integration",
        "sequence_length": 5,
        "canonical_form": "U_curve",
        "h1_requirement": "must_have_bottom_and_recovery"
    },
    "hero_journey": {
        "description": "Campbell's monomyth: ordinary → call → trials → revelation → return",
        "sequence_length": 7,
        "canonical_form": "departure_initiation_return",
        "h1_requirement": "must_have_threshold_crossing_and_return"
    },
    "rebirth": {
        "description": "Death and renewal: decline → death → gestation → emergence → flourishing",
        "sequence_length": 5,
        "canonical_form": "death_rebirth_cycle",
        "h1_requirement": "must_have_death_phase_and_emergence"
    },
    "quest": {
        "description": "Journey toward goal: preparation → journey → obstacles → achievement → consequences",
        "sequence_length": 5,
        "canonical_form": "linear_progression_with_trials",
        "h1_requirement": "must_have_goal_and_achievement"
    },
    "unresolved": {
        "description": "Suspended tension: equilibrium → disturbance → escalation → peak_ambiguity → suspension",
        "sequence_length": 5,
        "canonical_form": "rising_tension_held_open",
        "h1_requirement": "intentionally_incomplete_resolution_absent",
        "h1_note": "H¹ ≠ 0 by design — the missing resolution is the point. Audiences feel the pull toward closure that never arrives."
    }
}

# Affective dimension definitions
AFFECTIVE_DIMENSIONS = {
    "valence": {
        "range": (-1.0, 1.0),
        "description": "Pleasant (positive) to unpleasant (negative) feeling tone",
        "visual_encoding": "color_palette_and_lighting_warmth"
    },
    "arousal": {
        "range": (0.0, 1.0),
        "description": "Calm (low) to excited/agitated (high) energy level",
        "visual_encoding": "compositional_energy_and_contrast"
    },
    "dominance": {
        "range": (0.0, 1.0),
        "description": "Powerless (low) to in-control (high) agency",
        "visual_encoding": "scale_relationships_and_perspective"
    },
    "numinosity": {
        "range": (0.0, 1.0),
        "description": "Mundane (low) to sacred/overwhelming (high) significance",
        "visual_encoding": "lighting_quality_and_source_ambiguity"
    },
    "temporality": {
        "range": (0.0, 1.0),
        "description": "Timeless (low) to critical/irreversible (high) temporal pressure",
        "visual_encoding": "motion_blur_and_frame_density"
    }
}

# Canonical affective sequences (Layer 1 taxonomy)
TRAGEDY_AFFECTIVE_SEQUENCE = [
    {
        "position": "exposition",
        "valence": 0.6,
        "arousal": 0.3,
        "dominance": 0.7,
        "numinosity": 0.2,
        "temporality": 0.1,
        "narrative_function": "stability_before_fall"
    },
    {
        "position": "rising_action",
        "valence": 0.4,
        "arousal": 0.5,
        "dominance": 0.5,
        "numinosity": 0.4,
        "temporality": 0.4,
        "narrative_function": "control_slipping"
    },
    {
        "position": "climax",
        "valence": -0.8,
        "arousal": 0.9,
        "dominance": 0.1,
        "numinosity": 0.9,
        "temporality": 0.95,
        "narrative_function": "catastrophic_loss"
    },
    {
        "position": "falling_action",
        "valence": -0.6,
        "arousal": 0.6,
        "dominance": 0.2,
        "numinosity": 0.7,
        "temporality": 0.6,
        "narrative_function": "accepting_fate"
    },
    {
        "position": "denouement",
        "valence": -0.4,
        "arousal": 0.2,
        "dominance": 0.3,
        "numinosity": 0.5,
        "temporality": 0.1,
        "narrative_function": "somber_wisdom"
    }
]

COMEDY_AFFECTIVE_SEQUENCE = [
    {
        "position": "exposition",
        "valence": 0.5,
        "arousal": 0.3,
        "dominance": 0.6,
        "numinosity": 0.1,
        "temporality": 0.1,
        "narrative_function": "normal_world"
    },
    {
        "position": "complication",
        "valence": 0.0,
        "arousal": 0.6,
        "dominance": 0.3,
        "numinosity": 0.3,
        "temporality": 0.5,
        "narrative_function": "descent"
    },
    {
        "position": "crisis",
        "valence": -0.4,
        "arousal": 0.7,
        "dominance": 0.2,
        "numinosity": 0.6,
        "temporality": 0.8,
        "narrative_function": "bottom_of_U"
    },
    {
        "position": "reversal",
        "valence": 0.3,
        "arousal": 0.6,
        "dominance": 0.5,
        "numinosity": 0.4,
        "temporality": 0.6,
        "narrative_function": "upswing"
    },
    {
        "position": "resolution",
        "valence": 0.8,
        "arousal": 0.4,
        "dominance": 0.8,
        "numinosity": 0.2,
        "temporality": 0.1,
        "narrative_function": "integration_stronger_than_before"
    }
]

HERO_JOURNEY_AFFECTIVE_SEQUENCE = [
    {
        "position": "ordinary_world",
        "valence": 0.3,
        "arousal": 0.2,
        "dominance": 0.4,
        "numinosity": 0.1,
        "temporality": 0.1,
        "narrative_function": "mundane_stability"
    },
    {
        "position": "call_to_adventure",
        "valence": 0.2,
        "arousal": 0.6,
        "dominance": 0.3,
        "numinosity": 0.5,
        "temporality": 0.4,
        "narrative_function": "numinous_disruption"
    },
    {
        "position": "crossing_threshold",
        "valence": -0.1,
        "arousal": 0.7,
        "dominance": 0.4,
        "numinosity": 0.7,
        "temporality": 0.8,
        "narrative_function": "point_of_no_return"
    },
    {
        "position": "trials",
        "valence": -0.3,
        "arousal": 0.8,
        "dominance": 0.5,
        "numinosity": 0.6,
        "temporality": 0.7,
        "narrative_function": "ordeal_sequence"
    },
    {
        "position": "revelation",
        "valence": 0.1,
        "arousal": 0.9,
        "dominance": 0.7,
        "numinosity": 0.9,
        "temporality": 0.9,
        "narrative_function": "apotheosis"
    },
    {
        "position": "return",
        "valence": 0.5,
        "arousal": 0.5,
        "dominance": 0.8,
        "numinosity": 0.4,
        "temporality": 0.3,
        "narrative_function": "master_of_two_worlds"
    },
    {
        "position": "integration",
        "valence": 0.7,
        "arousal": 0.3,
        "dominance": 0.9,
        "numinosity": 0.3,
        "temporality": 0.1,
        "narrative_function": "transformed_ordinary"
    }
]

REBIRTH_AFFECTIVE_SEQUENCE = [
    {
        "position": "decline",
        "valence": 0.2,
        "arousal": 0.4,
        "dominance": 0.4,
        "numinosity": 0.3,
        "temporality": 0.3,
        "narrative_function": "vitality_fading"
    },
    {
        "position": "death",
        "valence": -0.7,
        "arousal": 0.3,
        "dominance": 0.1,
        "numinosity": 0.8,
        "temporality": 0.9,
        "narrative_function": "dissolution"
    },
    {
        "position": "gestation",
        "valence": -0.2,
        "arousal": 0.2,
        "dominance": 0.2,
        "numinosity": 0.7,
        "temporality": 0.2,
        "narrative_function": "dormancy_potential"
    },
    {
        "position": "emergence",
        "valence": 0.4,
        "arousal": 0.6,
        "dominance": 0.6,
        "numinosity": 0.8,
        "temporality": 0.7,
        "narrative_function": "breakthrough"
    },
    {
        "position": "flourishing",
        "valence": 0.8,
        "arousal": 0.5,
        "dominance": 0.9,
        "numinosity": 0.4,
        "temporality": 0.1,
        "narrative_function": "renewed_vitality"
    }
]

QUEST_AFFECTIVE_SEQUENCE = [
    {
        "position": "preparation",
        "valence": 0.5,
        "arousal": 0.5,
        "dominance": 0.7,
        "numinosity": 0.3,
        "temporality": 0.2,
        "narrative_function": "gathering_resources"
    },
    {
        "position": "journey",
        "valence": 0.3,
        "arousal": 0.6,
        "dominance": 0.6,
        "numinosity": 0.4,
        "temporality": 0.5,
        "narrative_function": "progress_toward_goal"
    },
    {
        "position": "obstacles",
        "valence": -0.2,
        "arousal": 0.8,
        "dominance": 0.4,
        "numinosity": 0.5,
        "temporality": 0.7,
        "narrative_function": "testing_resolve"
    },
    {
        "position": "achievement",
        "valence": 0.7,
        "arousal": 0.7,
        "dominance": 0.9,
        "numinosity": 0.6,
        "temporality": 0.8,
        "narrative_function": "goal_attained"
    },
    {
        "position": "consequences",
        "valence": 0.4,
        "arousal": 0.4,
        "dominance": 0.7,
        "numinosity": 0.4,
        "temporality": 0.2,
        "narrative_function": "cost_and_reward"
    }
]

UNRESOLVED_AFFECTIVE_SEQUENCE = [
    {
        "position": "equilibrium",
        "valence": 0.3,
        "arousal": 0.2,
        "dominance": 0.5,
        "numinosity": 0.15,
        "temporality": 0.1,
        "narrative_function": "surface_calm_concealing_fault_lines"
    },
    {
        "position": "disturbance",
        "valence": 0.0,
        "arousal": 0.5,
        "dominance": 0.4,
        "numinosity": 0.4,
        "temporality": 0.4,
        "narrative_function": "something_wrong_beneath_the_surface"
    },
    {
        "position": "escalation",
        "valence": -0.3,
        "arousal": 0.7,
        "dominance": 0.3,
        "numinosity": 0.6,
        "temporality": 0.7,
        "narrative_function": "forces_converging_no_exit"
    },
    {
        "position": "peak_ambiguity",
        "valence": -0.5,
        "arousal": 0.85,
        "dominance": 0.15,
        "numinosity": 0.85,
        "temporality": 0.95,
        "narrative_function": "maximum_uncertainty_all_outcomes_possible"
    },
    {
        "position": "suspension",
        "valence": -0.35,
        "arousal": 0.7,
        "dominance": 0.2,
        "numinosity": 0.75,
        "temporality": 0.85,
        "narrative_function": "held_at_the_edge_no_resolution"
    }
]

# Map arc types to sequences
AFFECTIVE_SEQUENCES = {
    "tragedy": TRAGEDY_AFFECTIVE_SEQUENCE,
    "comedy": COMEDY_AFFECTIVE_SEQUENCE,
    "hero_journey": HERO_JOURNEY_AFFECTIVE_SEQUENCE,
    "rebirth": REBIRTH_AFFECTIVE_SEQUENCE,
    "quest": QUEST_AFFECTIVE_SEQUENCE,
    "unresolved": UNRESOLVED_AFFECTIVE_SEQUENCE
}

# ============================================================================
# LAYER 2: DETERMINISTIC MAPPING (0 tokens)
# ============================================================================

def encode_affective_state_to_visual_parameters(affect_state: Dict) -> Dict:
    """
    Pure deterministic mapping: affective dimensions → visual parameters
    
    This is a morphism in the category of aesthetic parameters.
    No LLM calls, pure computation.
    """
    
    valence = affect_state["valence"]
    arousal = affect_state["arousal"]
    dominance = affect_state["dominance"]
    numinosity = affect_state["numinosity"]
    temporality = affect_state["temporality"]
    
    # Valence → Color palette
    if valence > 0.2:  # Positive: warm colors
        color_palette = {
            "type": "saturated_warm",
            "primaries": ["golden_yellow", "warm_orange", "soft_pink"],
            "saturation": 0.3 + (valence * 0.4),
            "temperature": "warm"
        }
    elif valence < -0.2:  # Negative: cool colors
        color_palette = {
            "type": "desaturated_cool",
            "primaries": ["slate_blue", "charcoal", "deep_teal"],
            "saturation": 0.3 + (abs(valence) * 0.4),  # Scale with magnitude like positive
            "temperature": "cool"
        }
    else:  # Neutral range: -0.2 to 0.2
        color_palette = {
            "type": "muted_neutral",
            "primaries": ["warm_gray", "soft_beige", "sage"],
            "saturation": 0.4,
            "temperature": "neutral"
        }
    
    # Arousal → Compositional energy
    composition = {
        "dynamic": arousal,
        "angles": "diagonal" if arousal > 0.6 else ("tilted" if arousal > 0.3 else "horizontal"),
        "contrast": int(arousal * 100),
        "edge_treatment": "sharp" if arousal > 0.7 else ("moderate" if arousal > 0.4 else "soft"),
        "visual_complexity": arousal * 10  # 0-10 scale
    }
    
    # Dominance → Scale relationships
    scale = {
        "subject_size": dominance,
        "environment_overwhelm": 1.0 - dominance,
        "perspective": "low_angle" if dominance > 0.6 else ("eye_level" if dominance > 0.3 else "high_angle"),
        "depth_compression": 1.0 - dominance  # Low dominance = compressed, overwhelming space
    }
    
    # Numinosity → Lighting quality
    lighting = {
        "quality": "radiant" if numinosity > 0.7 else ("atmospheric" if numinosity > 0.4 else "natural"),
        "intensity": numinosity,
        "source_ambiguity": numinosity,  # High numinosity = unclear where light comes from
        "god_rays": numinosity > 0.6,
        "atmospheric_glow": numinosity > 0.5
    }
    
    # Temporality → Motion and sharpness
    temporal = {
        "motion_blur": temporality * 0.5,  # Max 50% blur
        "sharpness": 1.0 - (temporality * 0.3),  # Maintain some sharpness
        "frame_density": temporality,  # High = packed moment
        "implied_velocity": temporality,
        "freeze_vs_flow": "frozen" if temporality > 0.8 else ("flowing" if temporality > 0.4 else "static")
    }
    
    return {
        "color_palette": color_palette,
        "composition": composition,
        "scale": scale,
        "lighting": lighting,
        "temporal": temporal,
        "affective_state": affect_state  # Include original for reference
    }

def calculate_h1_obstruction(sequence: List[Dict]) -> Dict:
    """
    Measure narrative cohomology: do affective states glue into complete arc?
    
    H¹ = 0: Complete narrative (all phases present)
    H¹ ≠ 0: Obstructions exist (missing phases)
    """
    
    required_phases = {
        "tragedy": ["exposition", "rising_action", "climax", "falling_action", "denouement"],
        "comedy": ["exposition", "complication", "crisis", "reversal", "resolution"],
        "hero_journey": ["ordinary_world", "call_to_adventure", "crossing_threshold", "trials", "revelation", "return", "integration"],
        "rebirth": ["decline", "death", "gestation", "emergence", "flourishing"],
        "quest": ["preparation", "journey", "obstacles", "achievement", "consequences"],
        "unresolved": ["equilibrium", "disturbance", "escalation", "peak_ambiguity", "suspension"]
    }

    # Arcs that are intentionally incomplete — H¹ ≠ 0 is a feature, not a defect
    intentionally_open = {
        "unresolved": {
            "absent_by_design": "resolution",
            "audience_effect": "pull_toward_closure_that_never_arrives",
            "social_media_function": "drives_shares_and_comments_seeking_resolution"
        }
    }
    
    # Detect arc type from sequence
    positions = [frame["position"] for frame in sequence]
    present_set = set(positions)
    
    # First try: Check for complete arc (100% match)
    detected_arc = None
    for arc_type, required in required_phases.items():
        if all(phase in positions for phase in required):
            detected_arc = arc_type
            break
    
    # Second try: Find best partial match (arc with most overlapping phases)
    if not detected_arc:
        best_match = None
        best_overlap = 0
        
        for arc_type, required in required_phases.items():
            required_set = set(required)
            overlap = len(present_set & required_set)
            
            # Track arc with most overlapping phases
            if overlap > best_overlap:
                best_overlap = overlap
                best_match = arc_type
        
        # If we have ANY recognized phases, use the best match
        if best_overlap > 0:
            detected_arc = best_match
        else:
            # NO recognized phases at all - truly unrecognized
            return {
                "h1_magnitude": 1.0,
                "obstruction": "unrecognized_arc_structure",
                "missing_phases": [],
                "narrative_complete": False
            }
    
    # Check for missing phases
    required_set = set(required_phases[detected_arc])
    missing = required_set - present_set

    h1_magnitude = len(missing) / len(required_set)

    result = {
        "h1_magnitude": h1_magnitude,
        "detected_arc": detected_arc,
        "missing_phases": list(missing),
        "narrative_complete": h1_magnitude == 0,
        "completeness": 1.0 - h1_magnitude,
        "obstruction": "incomplete_arc" if len(missing) > 0 else None
    }

    # Flag intentionally open arcs — H¹ ≠ 0 is structural, not a defect
    if detected_arc in intentionally_open:
        open_meta = intentionally_open[detected_arc]
        result["intentionally_open"] = True
        result["open_design"] = open_meta
        # Override obstruction label: this isn't a failure, it's the form
        if h1_magnitude == 0:
            result["narrative_complete"] = True  # all required phases present
            result["structural_tension"] = "resolution_absent_by_design"

    return result

def detect_compensation(sequence: List[Dict]) -> Dict:
    """
    Jung's prediction: Extreme unbalanced arcs will compensate
    
    Detect if sequence lacks recovery/resolution and predict compensation
    """
    
    # Extract valence trajectory
    valences = [frame["valence"] for frame in sequence]
    
    # Check for unrelenting negativity
    avg_valence = sum(valences) / len(valences)
    min_valence = min(valences)
    max_valence = max(valences)
    
    unrelenting_negative = (
        avg_valence < -0.5 and
        max_valence < 0.2 and
        len([v for v in valences if v < -0.4]) > len(valences) * 0.7
    )
    
    # Check for missing recovery arc
    last_third_valences = valences[-len(valences)//3:]
    recovery_present = any(v > valences[len(valences)//2] for v in last_third_valences)
    
    compensation_needed = unrelenting_negative or not recovery_present
    
    return {
        "compensation_needed": compensation_needed,
        "reason": "unrelenting_negativity" if unrelenting_negative else ("missing_recovery" if not recovery_present else "none"),
        "avg_valence": avg_valence,
        "valence_range": (min_valence, max_valence),
        "predicted_compensation": {
            "type": "spontaneous_relief_elements",
            "description": "System may introduce unexpected positive elements to complete arc"
        } if compensation_needed else None
    }

# ============================================================================
# LAYER 1 TOOLS: Taxonomy Discovery (0 tokens)
# ============================================================================

@mcp.tool()
def list_archetypal_arcs() -> str:
    """
    List all available archetypal narrative arcs with descriptions.
    
    Returns complete taxonomy of narrative structures.
    """
    
    result = {
        "archetypal_arcs": ARCHETYPAL_ARCS,
        "total_arcs": len(ARCHETYPAL_ARCS),
        "affective_dimensions": AFFECTIVE_DIMENSIONS
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
def get_affective_sequence(
    arc_type: Literal["tragedy", "comedy", "hero_journey", "rebirth", "quest", "unresolved"]
) -> str:
    """
    Get the canonical affective sequence for a specific archetypal arc.
    
    Returns frame-by-frame affective states.
    
    Args:
        arc_type: Which archetypal narrative structure
    """
    
    sequence = AFFECTIVE_SEQUENCES[arc_type]
    
    result = {
        "arc_type": arc_type,
        "description": ARCHETYPAL_ARCS[arc_type]["description"],
        "sequence_length": len(sequence),
        "affective_sequence": sequence,
        "h1_requirement": ARCHETYPAL_ARCS[arc_type]["h1_requirement"]
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
def get_affective_dimension_details(
    dimension: Literal["valence", "arousal", "dominance", "numinosity", "temporality"]
) -> str:
    """
    Get detailed information about a specific affective dimension.
    
    Args:
        dimension: Which affective dimension to examine
    """
    
    return json.dumps(AFFECTIVE_DIMENSIONS[dimension], indent=2)

# ============================================================================
# LAYER 2 TOOLS: Deterministic Mapping (0 tokens)
# ============================================================================

@mcp.tool()
def encode_affective_state(
    valence: float,
    arousal: float,
    dominance: float,
    numinosity: float,
    temporality: float
) -> str:
    """
    Convert affective state to concrete visual parameters (deterministic, 0 tokens).
    
    This is the core morphism: Affective Space → Visual Parameter Space
    
    Args:
        valence: -1.0 (unpleasant) to 1.0 (pleasant)
        arousal: 0.0 (calm) to 1.0 (excited)
        dominance: 0.0 (powerless) to 1.0 (in control)
        numinosity: 0.0 (mundane) to 1.0 (sacred/overwhelming)
        temporality: 0.0 (timeless) to 1.0 (critical moment)
    
    Returns:
        Complete visual parameter specification
    """
    
    affect_state = {
        "valence": valence,
        "arousal": arousal,
        "dominance": dominance,
        "numinosity": numinosity,
        "temporality": temporality
    }
    
    visual_params = encode_affective_state_to_visual_parameters(affect_state)
    
    return json.dumps(visual_params, indent=2)

@mcp.tool()
def calculate_narrative_cohomology(sequence_json: str) -> str:
    """
    Calculate H¹ obstruction for narrative sequence.
    
    Measures whether affective states glue into complete arc.
    
    Args:
        sequence_json: JSON array of affective states with "position" field
            [{"position": "exposition", "valence": 0.6, ...}, ...]
    
    Returns:
        H¹ magnitude and obstruction analysis
    """
    
    sequence = json.loads(sequence_json)
    h1_result = calculate_h1_obstruction(sequence)
    
    return json.dumps(h1_result, indent=2)

@mcp.tool()
def detect_compensatory_dynamics(sequence_json: str) -> str:
    """
    Detect if sequence requires Jungian compensation.
    
    Tests Jung's prediction: extreme unbalanced arcs self-regulate.
    
    Args:
        sequence_json: JSON array of affective states
    
    Returns:
        Compensation analysis and predictions
    """
    
    sequence = json.loads(sequence_json)
    compensation = detect_compensation(sequence)
    
    return json.dumps(compensation, indent=2)

# ============================================================================
# LAYER 3 TOOLS: Synthesis Context (~100-200 tokens)
# ============================================================================

@mcp.tool()
def generate_narrative_frame_spec(
    arc_type: Literal["tragedy", "comedy", "hero_journey", "rebirth", "quest", "unresolved"],
    frame_index: int,
    subject: str,
    semantic_coherence: Literal["random", "coherent"] = "random"
) -> str:
    """
    Generate complete specification for a single narrative frame.
    
    Combines:
    - Archetypal affective state (Layer 2)
    - Visual parameter encoding (Layer 2)
    - Subject matter (semantic layer)
    
    Ready for integration with other Lushy MCP servers or direct image generation.
    
    Args:
        arc_type: Which archetypal narrative
        frame_index: Position in sequence (0-based)
        subject: What to depict ("cat", "spaceship", etc.)
        semantic_coherence: Whether subject relates to narrative
    
    Returns:
        Complete frame specification with synthesis context
    """
    
    # Get affective state (Layer 1)
    sequence = AFFECTIVE_SEQUENCES[arc_type]
    
    if frame_index >= len(sequence):
        return json.dumps({
            "error": f"Frame index {frame_index} exceeds sequence length {len(sequence)}"
        })
    
    affect_state = sequence[frame_index]
    
    # Encode to visual parameters (Layer 2)
    visual_params = encode_affective_state_to_visual_parameters(affect_state)
    
    # Build synthesis context (Layer 3)
    synthesis_context = f"""
NARRATIVE FRAME SPECIFICATION

Arc Type: {arc_type}
Position: {affect_state['position']} (frame {frame_index + 1}/{len(sequence)})
Narrative Function: {affect_state['narrative_function']}

Subject: {subject}
Semantic Coherence: {semantic_coherence}

AFFECTIVE STATE:
- Valence: {affect_state['valence']:.2f} ({_describe_valence(affect_state['valence'])})
- Arousal: {affect_state['arousal']:.2f} ({_describe_arousal(affect_state['arousal'])})
- Dominance: {affect_state['dominance']:.2f} ({_describe_dominance(affect_state['dominance'])})
- Numinosity: {affect_state['numinosity']:.2f} ({_describe_numinosity(affect_state['numinosity'])})
- Temporality: {affect_state['temporality']:.2f} ({_describe_temporality(affect_state['temporality'])})

VISUAL ENCODING:

Color Palette: {visual_params['color_palette']['type']}
- Primaries: {', '.join(visual_params['color_palette']['primaries'])}
- Saturation: {visual_params['color_palette']['saturation']:.2f}
- Temperature: {visual_params['color_palette']['temperature']}

Composition:
- Dynamic level: {visual_params['composition']['dynamic']:.2f}
- Angles: {visual_params['composition']['angles']}
- Contrast: {visual_params['composition']['contrast']}%
- Edge treatment: {visual_params['composition']['edge_treatment']}

Scale & Perspective:
- Subject prominence: {visual_params['scale']['subject_size']:.2f}
- Environment pressure: {visual_params['scale']['environment_overwhelm']:.2f}
- Camera angle: {visual_params['scale']['perspective']}

Lighting:
- Quality: {visual_params['lighting']['quality']}
- Intensity: {visual_params['lighting']['intensity']:.2f}
- Source clarity: {'ambiguous' if visual_params['lighting']['source_ambiguity'] > 0.6 else 'clear'}
{"- God rays: YES" if visual_params['lighting']['god_rays'] else ""}

Temporal Treatment:
- Motion: {visual_params['temporal']['freeze_vs_flow']}
- Sharpness: {visual_params['temporal']['sharpness']:.2f}
- Implied velocity: {visual_params['temporal']['implied_velocity']:.2f}

NARRATIVE CONTEXT:
This frame represents the {affect_state['position']} phase of a {arc_type} arc.
Narrative function: {affect_state['narrative_function']}

H¹ REQUIREMENT: {ARCHETYPAL_ARCS[arc_type]['h1_requirement']}
"""
    
    result = {
        "arc_type": arc_type,
        "frame_index": frame_index,
        "position": affect_state['position'],
        "subject": subject,
        "affective_state": affect_state,
        "visual_parameters": visual_params,
        "synthesis_context": synthesis_context,
        "ready_for_generation": True
    }
    
    return json.dumps(result, indent=2)

@mcp.tool()
def generate_complete_narrative_sequence(
    arc_type: Literal["tragedy", "comedy", "hero_journey", "rebirth", "quest", "unresolved"],
    subjects: Optional[str] = None,  # JSON array or "random"
    semantic_coherence: Literal["random", "coherent"] = "random"
) -> str:
    """
    Generate specifications for complete narrative sequence.
    
    This is the main production tool for archetypal narrative generation.
    
    Args:
        arc_type: Which archetypal narrative structure
        subjects: JSON array of subjects per frame, or "random"
        semantic_coherence: Whether subjects form coherent story
    
    Returns:
        Complete sequence with all frame specifications and coherence analysis
    """
    
    sequence = AFFECTIVE_SEQUENCES[arc_type]
    
    # Handle subjects
    if subjects is None or subjects == "random":
        import random
        possible_subjects = [
            "cat", "spaceship", "coffee cup", "mountain", "lighthouse",
            "flower", "clock", "bridge", "mirror", "storm",
            "book", "window", "door", "tree", "ocean"
        ]
        subject_list = random.sample(possible_subjects, len(sequence))
    else:
        subject_list = json.loads(subjects)
        if len(subject_list) != len(sequence):
            return json.dumps({
                "error": f"Subject list length ({len(subject_list)}) doesn't match sequence length ({len(sequence)})"
            })
    
    # Generate frame specs
    frames = []
    for i, (affect_state, subject) in enumerate(zip(sequence, subject_list)):
        visual_params = encode_affective_state_to_visual_parameters(affect_state)
        
        frame_spec = {
            "frame_index": i,
            "position": affect_state['position'],
            "subject": subject,
            "affective_state": affect_state,
            "visual_parameters": visual_params
        }
        
        frames.append(frame_spec)
    
    # Calculate H¹
    h1_analysis = calculate_h1_obstruction(sequence)
    
    # Check compensation
    compensation_analysis = detect_compensation(sequence)
    
    result = {
        "arc_type": arc_type,
        "sequence_length": len(sequence),
        "semantic_coherence": semantic_coherence,
        "frames": frames,
        "cohomology_analysis": h1_analysis,
        "compensation_analysis": compensation_analysis,
        "ready_for_generation": True,
        "integration_note": "Use these frame specifications with image generation MCP servers or pass to tomographic orchestrator for structural feature integration"
    }
    
    return json.dumps(result, indent=2)

# ============================================================================
# INTEGRATION & INTENTIONALITY TOOLS
# ============================================================================

@mcp.tool()
def get_intentionality() -> str:
    """
    Explain WHY archetypal narrative structure works.
    
    Returns the theoretical foundation and empirical predictions.
    """
    
    intentionality = {
        "core_hypothesis": "Narrative coherence emerges from affective structure independent of semantic content",
        
        "jung_campbell_claim": "Archetypal narratives have invariant feeling tone trajectories that create coherence regardless of surface story",
        
        "empirical_prediction": "A sequence [cat → spaceship → coffee cup] following tragic affective arc will feel narratively coherent despite semantic randomness",
        
        "mechanisms": {
            "pre_verbal_recognition": "Affective pattern matching happens before semantic interpretation",
            "dimensional_encoding": "5D affective space (valence/arousal/dominance/numinosity/temporality) encodes complete narrative position",
            "phase_transition_criticality": "High temporality creates criticality where irreversible choices lock in",
            "compensatory_dynamics": "Extreme unbalanced arcs self-regulate per Jung's self-regulation principle"
        },
        
        "h1_cohomology_connection": {
            "h1_equals_zero": "Affective trajectory completes (exposition → climax → denouement glue)",
            "h1_not_zero": "Missing narrative phases create obstruction",
            "unrelenting_tragedy_test": "Maintaining climax without resolution creates H¹ ≠ 0 - system compensates or viewers perceive incompleteness"
        },
        
        "functor_structure": "Affective state → visual parameters is a morphism preserving archetypal structure",
        
        "glb_framework_connection": {
            "layer_1": "Valid visual compositions (taxonomy)",
            "layer_2": "Semantic coherence (relaxed in archetypal test)",
            "layer_3": "Affective structure (archetypal pattern)",
            "test": "Does Layer 3 alone create perceived narrative when Layer 2 is incoherent?"
        },
        
        "product_value": "Narrative Arc Generator bypasses prompt engineering by working at archetypal level rather than semantic level"
    }
    
    return json.dumps(intentionality, indent=2)

@mcp.tool()
def get_integration_bridges() -> str:
    """
    List how this server integrates with other Lushy MCP servers.
    """
    
    bridges = {
        "tomographic_orchestrator": {
            "integration": "Pass frame subjects through tomographic analysis to extract structural features",
            "workflow": "archetypal affective state → tomographic structural features → combined synthesis",
            "result": "Images with both archetypal narrative position AND structural coherence"
        },
        
        "norman_rockwell_mcp": {
            "integration": "Use narrative cohomology (H¹) to validate sequence completeness",
            "workflow": "Generate sequence → measure H¹ → detect obstructions → suggest interventions",
            "result": "Rockwell-quality narrative closure in image sequences"
        },
        
        "photographic_perspective_mcp": {
            "integration": "Map affective dimensions to camera parameters",
            "functor": "dominance → camera angle, arousal → focal length, numinosity → lighting quality",
            "result": "Camera positioning encodes narrative position"
        },
        
        "register_code_mcp": {
            "integration": "Affective state determines linguistic register for accompanying text",
            "functor": "valence/arousal → formality level, numinosity → technical density",
            "result": "Text accompanying images matches affective tone"
        },
        
        "shadow_complement_integration": {
            "integration": "Generate antipodal narrative sequences",
            "example": "tragedy → comedy (flip valence trajectory)",
            "result": "Explore narrative shadow through structural inversion"
        },
        
        "composition_graph_mcp": {
            "integration": "Validate which aesthetic domains compose well with archetypal arcs",
            "workflow": "Build adjacency matrix of affective states × aesthetic parameters",
            "result": "Optimal domain selection for narrative generation"
        }
    }
    
    return json.dumps(bridges, indent=2)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _describe_valence(v: float) -> str:
    if v > 0.6: return "highly pleasant"
    if v > 0.2: return "moderately pleasant"
    if v > -0.2: return "neutral"
    if v > -0.6: return "moderately unpleasant"
    return "highly unpleasant"

def _describe_arousal(a: float) -> str:
    if a > 0.7: return "highly aroused/agitated"
    if a > 0.4: return "moderately energized"
    return "calm/low energy"

def _describe_dominance(d: float) -> str:
    if d > 0.7: return "in control"
    if d > 0.3: return "moderate agency"
    return "powerless/overwhelmed"

def _describe_numinosity(n: float) -> str:
    if n > 0.7: return "sacred/overwhelming"
    if n > 0.4: return "portentous/significant"
    return "mundane"

def _describe_temporality(t: float) -> str:
    if t > 0.8: return "critical/irreversible moment"
    if t > 0.4: return "time pressure building"
    return "timeless/stable"

def main():
    mcp.run()

if __name__ == "__main__":
    main()

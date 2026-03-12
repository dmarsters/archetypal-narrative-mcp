# Archetypal Narrative MCP Server

Generate image sequences following Jung/Campbell archetypal narrative structures through deterministic affective state encoding.

## Installation
```bash
pip install archetypal-narrative-mcp
```

## Quick Start
```python
# Run as MCP server
archetypal-narrative-mcp

# Or programmatically
from archetypal_narrative_mcp.server import (
    TRAGEDY_AFFECTIVE_SEQUENCE,
    encode_affective_state_to_visual_parameters
)

# Get tragic arc
for frame in TRAGEDY_AFFECTIVE_SEQUENCE:
    visual_params = encode_affective_state_to_visual_parameters(frame)
    print(f"{frame['position']}: {visual_params}")
```

## Core Hypothesis

**Narrative coherence emerges from affective structure independent of semantic content.**

Test: A sequence [cat → spaceship → coffee cup → mountain] following a tragic affective arc should feel narratively coherent despite semantic randomness.

## Features

### Five Archetypal Arcs
- **Tragedy**: Stability → hubris → catastrophe → recognition → diminishment
- **Comedy**: Stability → disruption → crisis → reversal → integration  
- **Hero's Journey**: Ordinary → call → trials → revelation → return
- **Rebirth**: Decline → death → gestation → emergence → flourishing
- **Quest**: Preparation → journey → obstacles → achievement → consequences

### Five Affective Dimensions
- **Valence**: Unpleasant (-1.0) to pleasant (+1.0)
- **Arousal**: Calm (0.0) to excited (1.0)
- **Dominance**: Powerless (0.0) to in-control (1.0)
- **Numinosity**: Mundane (0.0) to sacred/overwhelming (1.0)
- **Temporality**: Timeless (0.0) to critical moment (1.0)

### Deterministic Visual Encoding
- Valence → Color palette & lighting warmth
- Arousal → Compositional energy & contrast
- Dominance → Scale relationships & perspective
- Numinosity → Lighting quality & source ambiguity
- Temporality → Motion blur & frame density

## Architecture

Three-layer olog pattern for cost optimization:

1. **Layer 1 (Taxonomy)**: Archetypal arc definitions - 0 tokens
2. **Layer 2 (Mapping)**: Affective state → visual parameters - 0 tokens
3. **Layer 3 (Synthesis)**: Context generation - ~150 tokens

**Cost savings**: 85% reduction vs pure LLM approaches

## Integration

Works seamlessly with other Lushy MCP servers:

- `tomographic-orchestrator`: Add structural features
- `norman-rockwell-mcp`: Validate narrative cohomology (H¹)
- `photographic-perspective-mcp`: Map affect to camera parameters
- `register-code-mcp`: Match linguistic register to affective tone

## Research Applications

Empirically test Jung/Campbell's claim that archetypal structures are recognized pre-verbally through affective pattern matching.

**Experimental Conditions**:
- Condition A: Random affect + random subject (no coherence)
- Condition B: Structured affect + random subject (test hypothesis)
- Condition C: Structured affect + coherent subject (baseline)
- Condition D: Random affect + coherent subject (control)

**Prediction**: Condition B shows narrative coherence despite semantic randomness.

## Documentation

- [Full documentation](https://github.com/dalmarsters/archetypal-narrative-mcp)
- [SKILL.md](https://github.com/dalmarsters/archetypal-narrative-mcp/blob/main/SKILL.md)
- [Research paper](https://github.com/dalmarsters/archetypal-narrative-mcp/docs/research.pdf)

## License

MIT License - See LICENSE file

## Citation
```bibtex
@software{archetypal_narrative_mcp,
  title={Archetypal Narrative MCP Server},
  author={Dal Marsters},
  year={2025},
  description={Jung/Campbell archetypal structures through affective encoding},
  url={https://github.com/dalmarsters/archetypal-narrative-mcp}
}
```

## Support

- GitHub Issues: https://github.com/dalmarsters/archetypal-narrative-mcp/issues
- Email: dal@lushy.app

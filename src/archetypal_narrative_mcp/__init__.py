# archetypal_narrative_mcp/__init__.py

"""
Archetypal Narrative MCP Server

Generate image sequences following Jung/Campbell archetypal narrative structures
through deterministic affective state encoding.

Three-Layer Architecture:
- Layer 1: Taxonomy (archetypal arcs, affective dimensions) - 0 tokens
- Layer 2: Deterministic mapping (affect → visual parameters) - 0 tokens  
- Layer 3: Synthesis context generation - ~150 tokens

Cost optimization: 85% zero-cost operations through categorical composition.
"""

__version__ = "1.0.0"
__author__ = "Dal Marsters"
__email__ = "dal@lushyai.com"

__all__ = [
    "__version__",
    "__author__", 
    "__email__",
]

# Export core constants and server instance for external use
from archetypal_narrative_mcp.server import (
    ARCHETYPAL_ARCS,
    AFFECTIVE_DIMENSIONS,
    AFFECTIVE_SEQUENCES,
    mcp,
)

__all__.extend([
    "ARCHETYPAL_ARCS",
    "AFFECTIVE_DIMENSIONS",
    "AFFECTIVE_SEQUENCES",
    "mcp",
])

"""
Configuration settings for DSSAT Viewer
"""
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment and initialization
DSSAT_BASE = None  # Will be populated during runtime
DSSAT_EXE = None   # Will be populated during runtime

# Default values
DEFAULT_ENCODING = 'utf-8'
FALLBACK_ENCODING = 'latin-1'

# Missing values for DSSAT files
MISSING_VALUES = {-99, -99.0, -99.9, -99.99, -99., '-99', '-99.0', '-99.9', '-99.99', '-99.'}

# UI Constants
DASH_PORT = 8050
DASH_HOST = "127.0.0.1"

# Plot styling
LINE_STYLES = ["solid", "dash", "dot", "dashdot"]
MARKER_SYMBOLS = ["circle", "square", "diamond", "triangle-up", "star"]
PLOT_COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

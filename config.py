# RayBug Configuration
# ===================
# This file contains all customizable settings for the RayBug logging tool.
# Modify these values to personalize your logging experience.

import os

# =============================================================================
# LOG DIRECTORY PATHS
# =============================================================================

# Directory for debug log files (errors, warnings, debug messages)
LOG_DIR_DEBUG = "logs/debug"

# Directory for user tracking log files (user actions, analytics)
LOG_DIR_USER_TRACKING = "logs/tracking"

# Ensure directories exist
os.makedirs(LOG_DIR_DEBUG, exist_ok=True)
os.makedirs(LOG_DIR_USER_TRACKING, exist_ok=True)

# =============================================================================
# CONSOLE OUTPUT CONTROL
# =============================================================================

# Set to True to show debug messages in console, False to suppress them
# Note: Error and warning messages always show in console regardless of this setting
DEBUG_TO_CONSOLE = True

# =============================================================================
# MESSAGE FORMATTING
# =============================================================================

# Character used to create decorative borders for title messages
# Examples: "~", "*", "=", "-", "#"
TITLE_BORDER_CHAR = "~"

# Number of border characters on each side of title text
# Example: With TITLE_BORDER_COUNT = 5, "Script Start" becomes "~~~~~ Script Start ~~~~~"
TITLE_BORDER_COUNT = 5

# Prefix character for non-title messages
# Examples: "-", "*", "•", "→", ">"
MESSAGE_PREFIX = "-"

# =============================================================================
# LOG FILE NAMING
# =============================================================================

# Date format for log file timestamps
# Examples: 
#   "%Y%m%d_%H%M%S" → 20250805_143045
#   "%Y-%m-%d_%H-%M-%S" → 2025-08-05_14-30-45
#   "%Y%m%d" → 20250805 (date only, multiple runs same day will overwrite)
LOG_TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"

# Log file name patterns (will be combined with timestamp)
DEBUG_LOG_NAME = "debug"       # Results in: debug_20250805_143045.log
TRACKING_LOG_NAME = "track"    # Results in: track_20250805_143045.log

# =============================================================================
# LOG FILE CONTENT FORMATTING
# =============================================================================

# Format for log file entries (uses Python logging format strings)
# Available variables: %(asctime)s, %(levelname)s, %(message)s, %(name)s
# Examples:
#   "%(asctime)s - %(levelname)s - %(message)s" → 2025-08-05 14:30:45,123 - DEBUG - - Message text
#   "[%(levelname)s] %(asctime)s: %(message)s" → [DEBUG] 2025-08-05 14:30:45,123: - Message text
#   "%(message)s" → - Message text (no timestamp or level in file)
FILE_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Format for console output (uses custom formatter in bug.py)
# This is handled by CustomConsoleFormatter class and shows: "LEVEL Message"

# =============================================================================
# ADVANCED SETTINGS
# =============================================================================

# Log file write mode
# "w" = overwrite existing log file each run
# "a" = append to existing log file
LOG_FILE_MODE = "w"

# Minimum log level for file output
# Options: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
FILE_LOG_LEVEL = "DEBUG"

# Minimum log level for console output  
# Options: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
CONSOLE_LOG_LEVEL = "DEBUG"

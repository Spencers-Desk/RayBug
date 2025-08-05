# RayBug - Advanced Logging Tool

**RayBug** is a standalone Python logging utility that provides flexible, dual-output logging capabilities with customizable formatters and multiple logging levels. This tool has been incorporated into the main **RayTools** project but can also be used independently.

## Features

- **Dual Logger System**: Separate loggers for debug information and user tracking
- **Timestamped Log Files**: Automatically generated log files with timestamp naming
- **Flexible Console Output**: Configurable console output with custom formatting
- **Multiple Debug Levels**: Support for error, warning, debug, and track levels
- **Title Formatting**: Special formatting for section titles with decorative borders
- **Conditional Console Output**: Debug messages can be conditionally shown on console

## Components

### Main Functions

- **`setup_logging(name, debug, console_output, log_dir)`**: Sets up a logger with file and optional console handlers
- **`bug(message, debug_level, title)`**: Main logging function with flexible formatting options

### Logger Types

1. **Debug Logger** (`logger_debug`): 
   - Handles error, warning, and debug messages
   - Outputs to both file and console (configurable)
   - File: `debug_YYYYMMDD_HHMMSS.log`

2. **Tracking Logger** (`logger_track`):
   - Handles user tracking messages
   - Outputs only to file (no console output)
   - File: `track_YYYYMMDD_HHMMSS.log`

## Configuration

RayBug uses a `config.py` file for all customizable settings. This allows you to personalize:

### File Paths
- **LOG_DIR_DEBUG**: Directory for debug log files
- **LOG_DIR_USER_TRACKING**: Directory for tracking log files

### Message Formatting
- **TITLE_BORDER_CHAR**: Character used for title borders (default: "~")
- **TITLE_BORDER_COUNT**: Number of border characters on each side (default: 5)
- **MESSAGE_PREFIX**: Prefix for non-title messages (default: "-")

### Console Output
- **DEBUG_TO_CONSOLE**: Show debug messages in console (default: True)
- **CONSOLE_LOG_LEVEL**: Minimum level for console output (default: "DEBUG")

### Log File Settings
- **LOG_TIMESTAMP_FORMAT**: Date format for log filenames (default: "%Y%m%d_%H%M%S")
- **DEBUG_LOG_NAME**: Name prefix for debug logs (default: "debug")
- **TRACKING_LOG_NAME**: Name prefix for tracking logs (default: "track")
- **FILE_LOG_FORMAT**: Format string for log file entries
- **FILE_LOG_LEVEL**: Minimum level for file output (default: "DEBUG")
- **LOG_FILE_MODE**: File write mode - "w" (overwrite) or "a" (append)

### Example config.py
```python
# Customize your logging experience
TITLE_BORDER_CHAR = "*"      # Use asterisks instead of tildes
TITLE_BORDER_COUNT = 3       # Shorter borders: *** Title ***
MESSAGE_PREFIX = "→"         # Use arrow prefix: → Message text
DEBUG_TO_CONSOLE = False     # Suppress debug console output
LOG_TIMESTAMP_FORMAT = "%Y-%m-%d_%H-%M-%S"  # Different date format
```

## Usage

### Basic Logging

```python
from bug import bug

# Simple debug message
bug("Processing data")

# Warning message
bug("Low memory warning", "warning")

# Error message
bug("File not found", "error")

# Tracking message (file only)
bug("User performed action X", "track")
```

### Title Messages

```python
# Create section titles with decorative borders
bug("Script Initialization", "debug", title=True)
# Output: "~~~~~ Script Initialization ~~~~~"
```

### Direct Logger Access

```python
from bug import logger_debug, logger_track

# Direct logger usage
logger_debug.info("Direct debug message")
logger_track.info("Direct tracking message")
```

## Log File Format

### Debug Log File
```
2025-08-05 14:30:45,123 - DEBUG - ~~~~~ Script started ~~~~~
2025-08-05 14:30:45,124 - DEBUG - - Processing patient data
2025-08-05 14:30:45,125 - WARNING - - Low memory warning
2025-08-05 14:30:45,126 - ERROR - - File not found
```

### Console Output
```
DEBUG ~~~~~ Script started ~~~~~
DEBUG - Processing patient data
WARNING - Low memory warning
ERROR - File not found
```

## Installation

1. Clone or download the `bug.py` file
2. Create a `config.py` file with required variables
3. Import and use in your Python scripts

## Integration with RayTools

This logging tool has been integrated into the larger **RayTools** project, providing consistent logging capabilities across all RayTools modules. When used within RayTools, the configuration is automatically handled by the main project settings.

## Dependencies

- Python 3.6
- Standard library modules: `logging`, `datetime`, `os`, `sys`
- Custom `config.py` file
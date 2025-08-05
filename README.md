# RayBug - Logging Tool

**RayBug** is a standalone Python logging utility. that provides flexible, dual-output logging capabilities with customizable formatters and multiple logging levels. This tool has been incorporated into the main **RayTools** project but can also be used independently.

**RayBug** is a byproduct of my main project, [RayTools](https://github.com/Spencers-Desk/RayTools), a toolbox designed to make working in RayStation much more efficient.

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
   - Tracks user actions
   - Outputs only to file (no console output)
   - File: `track_YYYYMMDD_HHMMSS.log`

## Configuration

RayBug uses a `config.py` file for all customizable settings. This allows you to personalize:

- File Paths
- Message Formatting
- Console Output
- Output File Settings

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

### F-String Support

```python
# Dynamic variables in messages
patient_id = "12345"
roi_count = 15
processing_time = 2.35

bug(f"Loading patient {patient_id}")
bug(f"Found {roi_count} ROIs in patient data", "debug")
bug(f"Processing completed in {processing_time:.2f} seconds", "debug", title=True)
bug(f"User {patient_id} accessed plan at {datetime.now()}", "track")

# Complex formatting
bug(f"Memory usage: {memory_used/1024/1024:.1f} MB / {memory_total/1024/1024:.1f} MB", "warning")
```

## Example Log File Format

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

1. Clone or download the `bug.py` and `config.py` files
2. Import and use in your Python scripts

## Dependencies

- Python 3.6
- Standard library modules: `logging`, `datetime`, `os`, `sys`
# RayBug Usage Examples

This document shows code examples and their expected outputs for the RayBug logging tool.

## Basic Debug Message

```python
bug("Loading patient data from database", "debug")
```

**Console Output:** (with default config: MESSAGE_PREFIX="-")
```
DEBUG - Loading patient data from database
```

**With Custom Config:** (MESSAGE_PREFIX="→")
```
DEBUG → Loading patient data from database
```

**Log File Output:**
```
2025-08-05 14:30:45,123 - DEBUG - - Loading patient data from database
```

---

## Title Message

```python
bug("Medical Image Processing Script", "debug", title=True)
```

**Console Output:** (with default config: TITLE_BORDER_CHAR="~", TITLE_BORDER_COUNT=5)
```
DEBUG ~~~~~ Medical Image Processing Script ~~~~~
```

**Log File Output:**
```
2025-08-05 14:30:45,124 - DEBUG - ~~~~~ Medical Image Processing Script ~~~~~
```

**With Custom Config:** (TITLE_BORDER_CHAR="*", TITLE_BORDER_COUNT=3)
```
DEBUG *** Medical Image Processing Script ***
```

---

## Warning Message

```python
bug("Memory usage is getting high", "warning")
```

**Console Output:**
```
WARNING - Memory usage is getting high
```

**Log File Output:**
```
2025-08-05 14:30:45,125 - WARNING - - Memory usage is getting high
```

---

## Error Message

```python
bug("Failed to load configuration file", "error")
```

**Console Output:**
```
ERROR - Failed to load configuration file
```

**Log File Output:**
```
2025-08-05 14:30:45,126 - ERROR - - Failed to load configuration file
```

---

## Tracking Message (File Only)

```python
bug("User opened patient plan", "track")
```

**Console Output:**
```
(No console output - tracking messages only go to log file)
```

**Tracking Log File Output:**
```
2025-08-05 14:30:45,127 - INFO - - User opened patient plan
```

---

## Warning Title

```python
bug("Configuration Issues Found", "warning", title=True)
```

**Console Output:**
```
WARNING ~~~~~ Configuration Issues Found ~~~~~
```

**Log File Output:**
```
2025-08-05 14:30:45,128 - WARNING - ~~~~~ Configuration Issues Found ~~~~~
```

---

## Error Title

```python
bug("Critical System Error", "error", title=True)
```

**Console Output:**
```
ERROR ~~~~~ Critical System Error ~~~~~
```

**Log File Output:**
```
2025-08-05 14:30:45,129 - ERROR - ~~~~~ Critical System Error ~~~~~
```

---

## Workflow Example

```python
bug("Image Processing Phase", "debug", title=True)
bug("Applying noise reduction filters", "debug")
bug("Segmenting anatomical structures", "debug")
bug("User applied manual correction to contour", "track")
bug("Processing completed successfully", "debug")
```

**Console Output:**
```
DEBUG ~~~~~ Image Processing Phase ~~~~~
DEBUG - Applying noise reduction filters
DEBUG - Segmenting anatomical structures
DEBUG - Processing completed successfully
```

**Debug Log File Output:**
```
2025-08-05 14:30:45,130 - DEBUG - ~~~~~ Image Processing Phase ~~~~~
2025-08-05 14:30:45,131 - DEBUG - - Applying noise reduction filters
2025-08-05 14:30:45,132 - DEBUG - - Segmenting anatomical structures
2025-08-05 14:30:45,135 - DEBUG - - Processing completed successfully
```

**Tracking Log File Output:**
```
2025-08-05 14:30:45,133 - INFO - - User applied manual correction to contour
```

---

## Notes

- **Debug messages** appear in both console and debug log file
- **Warning/Error messages** always appear in both console and debug log file
- **Track messages** only appear in the tracking log file (no console output)
- **Title formatting** uses configurable border characters and count
- **Non-title messages** use configurable prefix character
- **Log files** include timestamps, while console output shows only level and message
- **All formatting** can be customized via config.py settings
- **Console output** can be controlled via `DEBUG_TO_CONSOLE` setting in config.py

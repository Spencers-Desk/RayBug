"""
RayBug Example - Simple Runnable Demo
====================================

Run this file to see the RayBug logging tool in action.
This will create log files and show console output.

Make sure config.py exists in the same directory before running.
"""

# Import the bug function
from bug import bug

if __name__ == "__main__":
    print("RayBug Demo - Running examples...\n")
    
    # Basic debug message
    bug("Loading patient data from database", "debug")
    
    # Title message
    bug("Medical Image Processing Script", "debug", title=True)
    
    # Warning message
    bug("Memory usage is getting high", "warning")
    
    # Error message
    bug("Failed to load configuration file", "error")
    
    # Tracking message (file only)
    bug("User opened patient plan", "track")
    
    # More workflow examples
    bug("Image Processing Phase", "debug", title=True)
    bug("Applying noise reduction filters", "debug")
    bug("Segmenting anatomical structures", "debug")
    bug("User applied manual correction to contour", "track")
    bug("Processing completed successfully", "debug")
    
    print("\nDemo complete! Check the logs directory for generated files:")

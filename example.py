"""
RayBug Example - RayStation Workflow Demo
=========================================

Run this file to see the RayBug logging tool in action with realistic
RayStation treatment planning workflow scenarios.

Make sure config.py exists in the same directory before running.
"""

import datetime

# Import the bug function
from bug import bug

if __name__ == "__main__":
    print("RayBug Demo - RayStation Workflow Examples...\n")
    
    # Session initialization
    bug("RayStation Treatment Planning Session", "debug", title=True)
    bug("Loading patient database connection", "debug")
    
    # Patient and case management
    patient_id = "MRN_12345"
    case_name = "Prostate_IMRT"
    bug(f"User opened patient {patient_id}", "track")
    bug(f"Loading case: {case_name}", "debug")
    bug(f"Patient {patient_id} case {case_name} loaded successfully", "track")
    
    # Structure creation and contouring
    bug("Structure Set Management", "debug", title=True)
    bug("User created PTV_Eval_High-03", "track")
    bug("User created PTV_Eval_Low-02", "track")
    bug("Importing physician contours from DICOM", "debug")
    bug("User modified CTV_High contour on slice 15", "track")
    bug("User created OAR_Rectum_PRV with 3mm expansion", "track")
    
    # Planning workflow
    bug("Treatment Planning Phase", "debug", title=True)
    bug("User initiated auto planning for IMRT technique", "track")
    bug("Optimizing dose distribution - iteration 1", "debug")
    bug("Optimizing dose distribution - iteration 2", "debug")
    
    # Dose calculations
    planning_time = 4.2
    bug(f"Dose calculation completed in {planning_time:.1f} minutes", "debug")
    bug("User reviewed dose color wash display", "track")
    
    # Plan evaluation
    bug("Plan Evaluation", "debug", title=True)
    bug("Calculating DVH statistics", "debug")
    bug("User opened DVH analysis window", "track")
    ptv_coverage = 98.7
    bug(f"PTV coverage: {ptv_coverage:.1f}% at prescription dose", "debug")
    
    # QA and export
    bug("Quality Assurance", "debug", title=True)
    bug("Running plan complexity analysis", "debug")
    bug("User approved treatment plan", "track")
    bug("User exported plan to treatment delivery system", "track")
    bug("Plan export completed successfully", "debug")
    
    # Session completion
    bug(f"Treatment planning session completed at {datetime.datetime.now().strftime('%H:%M:%S')}", "debug")
    
    print("\nDemo complete! Check the logs directory for generated files:")
    print("- Debug log shows technical workflow steps")
    print("- Tracking log shows user actions for audit trail")

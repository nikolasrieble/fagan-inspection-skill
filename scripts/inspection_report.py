#!/usr/bin/env python3
"""
Fagan Inspection Report Generator

Generates formal inspection reports following the Fagan methodology.
Produces three types of outputs:
1. Error List - Detailed description of each error
2. Module Detail Report - Error counts by type, severity, category
3. Inspection Summary Report - Overall metrics and signatures

Usage:
    python inspection_report.py --help
    python inspection_report.py --interactive
    python inspection_report.py --from-file errors.json
"""

import argparse
import json
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional
from collections import defaultdict

# Valid error classification values
VALID_ERROR_TYPES = {
    "LO", "IC", "IR", "TB", "DE", "PR", "PU", "MN", 
    "PE", "CC", "CU", "DA", "RU", "SU", "ST", "MA", "MD", "OT"
}
VALID_CATEGORIES = {"M", "W", "E"}
VALID_SEVERITIES = {"MAJ", "MIN"}
MAJOR_ERROR_THRESHOLD = 5  # Threshold for reinspection fallback


class Error:
    """Represents a single error found during inspection."""
    
    def __init__(self, number: int, location: str, error_type: str, 
                 category: str, severity: str, description: str, 
                 solution: str = ""):
        # Validate inputs
        if error_type.upper() not in VALID_ERROR_TYPES:
            raise ValueError(f"Invalid error type '{error_type}'. Must be one of: {', '.join(sorted(VALID_ERROR_TYPES))}")
        if category.upper() not in VALID_CATEGORIES:
            raise ValueError(f"Invalid category '{category}'. Must be one of: {', '.join(sorted(VALID_CATEGORIES))}")
        if severity.upper() not in VALID_SEVERITIES:
            raise ValueError(f"Invalid severity '{severity}'. Must be one of: {', '.join(sorted(VALID_SEVERITIES))}")
        
        self.number = number
        self.location = location  # file:line or module:function:line
        self.error_type = error_type.upper()  # LO, IC, TB, etc.
        self.category = category.upper()  # M, W, E
        self.severity = severity.upper()  # MAJ, MIN
        self.description = description
        self.solution = solution
    
    def classification(self) -> str:
        """Return full classification string."""
        return f"{self.error_type}/{self.category}/{self.severity}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "number": self.number,
            "location": self.location,
            "type": self.error_type,
            "category": self.category,
            "severity": self.severity,
            "classification": self.classification(),
            "description": self.description,
            "solution": self.solution
        }


class InspectionReport:
    """Generates Fagan inspection reports."""
    
    def __init__(self, inspection_id: str, inspection_type: str, 
                 module_name: str, inspection_date: Optional[str] = None):
        self.inspection_id = inspection_id
        self.inspection_type = inspection_type  # I0, I1, I2, I3, etc.
        self.module_name = module_name
        self.inspection_date = inspection_date or datetime.now().strftime("%Y-%m-%d")
        self.errors: List[Error] = []
        self.participants: List[str] = []
        self.metrics: Dict[str, Any] = {
            "eloc_estimate_pre": 0,
            "eloc_estimate_post": 0,
            "preparation_hours": 0,
            "meeting_hours": 0,
            "rework_hours": 0,
            "followup_hours": 0
        }
    
    def add_error(self, error: Error):
        """Add an error to the report."""
        self.errors.append(error)
    
    def add_participant(self, name: str, role: str):
        """Add a participant to the inspection."""
        self.participants.append(f"{name} ({role})")
    
    def set_metrics(self, **kwargs):
        """Set inspection metrics."""
        self.metrics.update(kwargs)
    
    def generate_error_list(self) -> str:
        """Generate detailed error list (Report Type 7A)."""
        output = []
        output.append("=" * 80)
        output.append(f"INSPECTION ERROR LIST - {self.inspection_id}")
        output.append("=" * 80)
        output.append(f"Module: {self.module_name}")
        output.append(f"Inspection Type: {self.inspection_type}")
        output.append(f"Date: {self.inspection_date}")
        output.append(f"Total Errors: {len(self.errors)}")
        output.append("=" * 80)
        output.append("")
        
        for error in self.errors:
            output.append(f"Error #{error.number:03d}")
            output.append(f"Location: {error.location}")
            output.append(f"Classification: {error.classification()}")
            output.append(f"Description:")
            output.append(f"  {error.description}")
            if error.solution:
                output.append(f"Possible Solution:")
                output.append(f"  {error.solution}")
            output.append("-" * 80)
            output.append("")
        
        return "\n".join(output)
    
    def generate_module_detail(self) -> str:
        """Generate module detail report (Report Type 7B)."""
        # Count errors by type, category, severity
        type_counts = defaultdict(int)
        category_counts = defaultdict(int)
        severity_counts = defaultdict(int)
        
        for error in self.errors:
            type_counts[error.error_type] += 1
            category_counts[error.category] += 1
            severity_counts[error.severity] += 1
        
        output = []
        output.append("=" * 80)
        output.append(f"MODULE DETAIL REPORT - {self.inspection_id}")
        output.append("=" * 80)
        output.append(f"Module: {self.module_name}")
        output.append(f"Inspection Type: {self.inspection_type}")
        output.append(f"Date: {self.inspection_date}")
        output.append("=" * 80)
        output.append("")
        
        # Error summary
        output.append("ERROR SUMMARY")
        output.append("-" * 40)
        output.append(f"Total Errors: {len(self.errors)}")
        output.append(f"Major: {severity_counts['MAJ']}")
        output.append(f"Minor: {severity_counts['MIN']}")
        output.append("")
        
        # Errors by type
        output.append("ERRORS BY TYPE")
        output.append("-" * 40)
        for error_type in sorted(type_counts.keys()):
            count = type_counts[error_type]
            output.append(f"{error_type:4s}: {count:3d}")
        output.append("")
        
        # Errors by category
        output.append("ERRORS BY CATEGORY")
        output.append("-" * 40)
        for cat in sorted(category_counts.keys()):
            count = category_counts[cat]
            cat_name = {"M": "Missing", "W": "Wrong", "E": "Extra"}.get(cat, "Unknown")
            output.append(f"{cat} ({cat_name:8s}): {count:3d}")
        output.append("")
        
        # Calculate reinspection need
        if self.metrics.get("eloc_estimate_pre", 0) > 0:
            eloc_reworked = abs(self.metrics.get("eloc_estimate_post", 0) - 
                               self.metrics.get("eloc_estimate_pre", 0))
            rework_percentage = (eloc_reworked / self.metrics["eloc_estimate_pre"]) * 100
            reinspection_needed = rework_percentage > 5
        else:
            # Fallback when ELOC data unavailable: use major error count threshold
            # Note: This is a heuristic and not aligned with Fagan's percentage-based approach
            reinspection_needed = len([e for e in self.errors if e.severity == "MAJ"]) > MAJOR_ERROR_THRESHOLD
        
        output.append("REINSPECTION DECISION")
        output.append("-" * 40)
        output.append(f"Reinspection Required: {'YES' if reinspection_needed else 'NO'}")
        if reinspection_needed:
            output.append("Reason: >5% of material reworked or >5 major errors")
        output.append("")
        
        return "\n".join(output)
    
    def generate_summary(self) -> str:
        """Generate inspection summary report (Report Type 7C)."""
        output = []
        output.append("=" * 80)
        output.append(f"INSPECTION SUMMARY REPORT - {self.inspection_id}")
        output.append("=" * 80)
        output.append(f"Module: {self.module_name}")
        output.append(f"Inspection Type: {self.inspection_type}")
        output.append(f"Date: {self.inspection_date}")
        output.append("=" * 80)
        output.append("")
        
        # Participants
        output.append("PARTICIPANTS")
        output.append("-" * 40)
        for participant in self.participants:
            output.append(f"  {participant}")
        output.append("")
        
        # Size estimates
        output.append("SIZE ESTIMATES (ELOC)")
        output.append("-" * 40)
        output.append(f"Pre-inspection:  {self.metrics.get('eloc_estimate_pre', 0):6d}")
        output.append(f"Post-inspection: {self.metrics.get('eloc_estimate_post', 0):6d}")
        output.append(f"Rework estimate: {abs(self.metrics.get('eloc_estimate_post', 0) - self.metrics.get('eloc_estimate_pre', 0)):6d}")
        output.append("")
        
        # Effort
        output.append("EFFORT (PERSON-HOURS)")
        output.append("-" * 40)
        prep = self.metrics.get('preparation_hours', 0)
        meet = self.metrics.get('meeting_hours', 0)
        rework = self.metrics.get('rework_hours', 0)
        followup = self.metrics.get('followup_hours', 0)
        total = prep + meet + rework + followup
        
        output.append(f"Preparation: {prep:6.1f}")
        output.append(f"Meeting:     {meet:6.1f}")
        output.append(f"Rework:      {rework:6.1f}")
        output.append(f"Follow-up:   {followup:6.1f}")
        output.append(f"Total:       {total:6.1f}")
        output.append("")
        
        # Error summary
        major_count = len([e for e in self.errors if e.severity == "MAJ"])
        minor_count = len([e for e in self.errors if e.severity == "MIN"])
        
        output.append("ERROR SUMMARY")
        output.append("-" * 40)
        output.append(f"Major errors:  {major_count:3d}")
        output.append(f"Minor errors:  {minor_count:3d}")
        output.append(f"Total errors:  {len(self.errors):3d}")
        output.append("")
        
        # Metrics
        if self.metrics.get('eloc_estimate_pre', 0) > 0:
            errors_per_kloc = (len(self.errors) / self.metrics['eloc_estimate_pre']) * 1000
            output.append("QUALITY METRICS")
            output.append("-" * 40)
            output.append(f"Errors per K.LOC: {errors_per_kloc:6.2f}")
            
            if meet > 0:
                inspection_rate = self.metrics['eloc_estimate_pre'] / meet
                output.append(f"Inspection rate:  {inspection_rate:6.0f} LOC/hour")
            output.append("")
        
        # Signatures
        output.append("SIGN-OFF")
        output.append("-" * 40)
        output.append("Designer:    _________________________  Date: __________")
        output.append("Programmer:  _________________________  Date: __________")
        output.append("Team Leader: _________________________  Date: __________")
        output.append("Moderator:   _________________________  Date: __________")
        output.append("")
        
        return "\n".join(output)
    
    def export_json(self) -> str:
        """Export report data as JSON."""
        data = {
            "inspection_id": self.inspection_id,
            "inspection_type": self.inspection_type,
            "module_name": self.module_name,
            "inspection_date": self.inspection_date,
            "participants": self.participants,
            "metrics": self.metrics,
            "errors": [error.to_dict() for error in self.errors]
        }
        return json.dumps(data, indent=2)


def interactive_mode():
    """Run interactive report generation."""
    print("=" * 80)
    print("Fagan Inspection Report Generator - Interactive Mode")
    print("=" * 80)
    print()
    
    # Basic info
    inspection_id = input("Inspection ID (e.g., I2-MOD123-2024-01): ")
    inspection_type = input("Inspection Type (I0/I1/I2/I3): ")
    module_name = input("Module/Component Name: ")
    
    report = InspectionReport(inspection_id, inspection_type, module_name)
    
    # Participants
    print("\nParticipants (press Enter with empty name to finish):")
    while True:
        name = input("  Name: ")
        if not name:
            break
        role = input("  Role (Moderator/Designer/Coder/Tester): ")
        report.add_participant(name, role)
    
    # Metrics
    print("\nMetrics:")
    report.set_metrics(
        eloc_estimate_pre=int(input("  ELOC estimate (pre-inspection): ") or "0"),
        eloc_estimate_post=int(input("  ELOC estimate (post-inspection): ") or "0"),
        preparation_hours=float(input("  Preparation hours: ") or "0"),
        meeting_hours=float(input("  Meeting hours: ") or "0"),
        rework_hours=float(input("  Rework hours (estimate): ") or "0"),
        followup_hours=float(input("  Follow-up hours (estimate): ") or "0")
    )
    
    # Errors
    print("\nErrors (press Enter with empty description to finish):")
    error_num = 1
    while True:
        print(f"\n  Error #{error_num}:")
        description = input("    Description: ")
        if not description:
            break
        
        location = input("    Location (file:line): ")
        error_type = input("    Type (LO/IC/TB/DE/PR/etc.): ")
        category = input("    Category (M/W/E): ")
        severity = input("    Severity (MAJ/MIN): ")
        solution = input("    Possible solution (optional): ")
        
        error = Error(error_num, location, error_type, category, severity, 
                     description, solution)
        report.add_error(error)
        error_num += 1
    
    return report


def load_from_file(filepath: str) -> InspectionReport:
    """Load inspection data from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    report = InspectionReport(
        data['inspection_id'],
        data['inspection_type'],
        data['module_name'],
        data.get('inspection_date')
    )
    
    for participant in data.get('participants', []):
        report.participants.append(participant)
    
    report.set_metrics(**data.get('metrics', {}))
    
    for error_data in data.get('errors', []):
        error = Error(
            error_data['number'],
            error_data['location'],
            error_data['type'],
            error_data['category'],
            error_data['severity'],
            error_data['description'],
            error_data.get('solution', '')
        )
        report.add_error(error)
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate Fagan inspection reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python inspection_report.py --interactive

  # Load from JSON file
  python inspection_report.py --from-file errors.json

  # Generate all report types
  python inspection_report.py --from-file errors.json --output-dir ./reports

Report Types:
  error-list     - Detailed list of all errors (7A)
  module-detail  - Error counts by type/category/severity (7B)
  summary        - Overall inspection summary (7C)
  json           - Raw data export
        """
    )
    
    parser.add_argument('--interactive', action='store_true',
                       help='Run in interactive mode')
    parser.add_argument('--from-file', metavar='FILE',
                       help='Load inspection data from JSON file')
    parser.add_argument('--output-dir', metavar='DIR', default='.',
                       help='Output directory for reports (default: current directory)')
    parser.add_argument('--report-type', 
                       choices=['error-list', 'module-detail', 'summary', 'json', 'all'],
                       default='all',
                       help='Type of report to generate (default: all)')
    
    args = parser.parse_args()
    
    # Get report
    if args.interactive:
        report = interactive_mode()
    elif args.from_file:
        report = load_from_file(args.from_file)
    else:
        parser.print_help()
        return
    
    # Generate reports
    import os
    os.makedirs(args.output_dir, exist_ok=True)
    
    base_name = f"{report.inspection_id}"
    
    if args.report_type in ('error-list', 'all'):
        output = report.generate_error_list()
        filepath = os.path.join(args.output_dir, f"{base_name}_error-list.txt")
        with open(filepath, 'w') as f:
            f.write(output)
        print(f"Error list written to: {filepath}")
    
    if args.report_type in ('module-detail', 'all'):
        output = report.generate_module_detail()
        filepath = os.path.join(args.output_dir, f"{base_name}_module-detail.txt")
        with open(filepath, 'w') as f:
            f.write(output)
        print(f"Module detail written to: {filepath}")
    
    if args.report_type in ('summary', 'all'):
        output = report.generate_summary()
        filepath = os.path.join(args.output_dir, f"{base_name}_summary.txt")
        with open(filepath, 'w') as f:
            f.write(output)
        print(f"Summary written to: {filepath}")
    
    if args.report_type in ('json', 'all'):
        output = report.export_json()
        filepath = os.path.join(args.output_dir, f"{base_name}_data.json")
        with open(filepath, 'w') as f:
            f.write(output)
        print(f"JSON data written to: {filepath}")


if __name__ == '__main__':
    main()

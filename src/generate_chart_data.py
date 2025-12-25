#!/usr/bin/env python3
"""
Wazuh Dashboard Lite - Alert Data Processor
Processes Wazuh alerts and generates visualization data.
"""

import json
import argparse
import sys
from pathlib import Path

def process_alerts_file(alert_path):
    """Process alerts from a local JSON file."""
    # Tu código existente aquí
    pass

def process_alerts_api(api_url, username, password):
    """Process alerts from Wazuh API."""
    # Implementación futura
    pass

def generate_sample_data():
    """Generate sample data for testing/demo."""
    sample_data = {
        "labels": ["192.168.1.10", "10.0.0.5", "172.16.0.20"],
        "datasets": [
            {
                "label": "Failed Attempts",
                "data": [15, 8, 23],
                "backgroundColor": "#4e73df"
            },
            {
                "label": "Malware Detected",
                "data": [2, 0, 5],
                "backgroundColor": "#e74a3b"
            }
        ]
    }
    return sample_data

def main():
    parser = argparse.ArgumentParser(description="Wazuh Dashboard Lite - Alert Processor")
    parser.add_argument("--source", choices=["file", "api", "sample"], 
                       default="file", help="Data source (default: file)")
    parser.add_argument("--path", default="/var/ossec/logs/alerts/alerts.json",
                       help="Path to alerts JSON file")
    parser.add_argument("--output", default="examples/wazuh_chart_data_enhanced.json",
                       help="Output JSON file path")
    parser.add_argument("--sample", action="store_true",
                       help="Generate sample data (for testing)")
    
    args = parser.parse_args()
    
    if args.sample or args.source == "sample":
        data = generate_sample_data()
        print("✓ Generated sample data")
    elif args.source == "file":
        data = process_alerts_file(args.path)
        print(f"✓ Processed alerts from {args.path}")
    elif args.source == "api":
        print("API processing not yet implemented")
        sys.exit(1)
    
    # Save output
    with open(args.output, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Data saved to {args.output}")
    print(f"  - {len(data.get('labels', []))} IP addresses")
    print(f"  - {len(data.get('datasets', []))} alert categories")

if __name__ == "__main__":
    main()

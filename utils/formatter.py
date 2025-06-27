import json
import csv
import os

def export_to_json(data, output_path="reports/report.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] JSON report saved: {output_path}")
    except Exception as e:
        print(f"[!] Failed to write JSON: {e}")

def export_to_csv(data, output_path="reports/report.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        with open(output_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"[+] CSV report saved: {output_path}")
    except Exception as e:
        print(f"[!] Failed to write CSV: {e}")

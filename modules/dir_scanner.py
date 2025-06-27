import os
import hashlib
import time
import platform
from utils.formatter import export_to_json, export_to_csv

from utils.formatter import export_to_json, export_to_csv
# Keep other imports

def scan_directory_web(root_dir):
    if not os.path.isdir(root_dir):
        return {"error": "Directory not found."}

    results = []

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_info = {
                "path": file_path,
                "size": None,
                "sha256": None,
                "created": None,
                "modified": None,
                "accessed": None,
            }

            try:
                file_info["size"] = os.path.getsize(file_path)
                with open(file_path, "rb") as f:
                    file_info["sha256"] = hashlib.sha256(f.read()).hexdigest()

                access_time = os.path.getatime(file_path)
                modified_time = os.path.getmtime(file_path)
                if platform.system() == "Windows":
                    created_time = os.path.getctime(file_path)
                else:
                    created_time = os.stat(file_path).st_birthtime if hasattr(os.stat(file_path), 'st_birthtime') else None

                if created_time:
                    file_info["created"] = time.ctime(created_time)
                file_info["modified"] = time.ctime(modified_time)
                file_info["accessed"] = time.ctime(access_time)

            except Exception as e:
                file_info["error"] = str(e)

            results.append(file_info)

    # Also export reports
    export_to_json(results, "reports/web_report.json")
    export_to_csv(results, "reports/web_report.csv")

    return results

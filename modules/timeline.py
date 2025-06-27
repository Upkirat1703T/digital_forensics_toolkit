import os
import time
import platform

import os
import time
import platform

def get_file_timeline_web(file_path):
    if not os.path.isfile(file_path):
        return {"error": "File not found."}

    try:
        timeline = {}
        access_time = os.path.getatime(file_path)
        modified_time = os.path.getmtime(file_path)

        if platform.system() == "Windows":
            created_time = os.path.getctime(file_path)
        else:
            created_time = os.stat(file_path).st_birthtime if hasattr(os.stat(file_path), 'st_birthtime') else None

        if created_time:
            timeline["Created"] = time.ctime(created_time)
        else:
            timeline["Created"] = "Not available"

        timeline["Modified"] = time.ctime(modified_time)
        timeline["Accessed"] = time.ctime(access_time)
        return timeline

    except Exception as e:
        return {"error": f"Timeline extraction error: {e}"}

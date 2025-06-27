from flask import Flask, render_template, request, send_file
import os
import zipfile
import uuid

from modules import hasher, metadata_extractor, timeline, dir_scanner


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        task = request.form.get("task")
        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            return render_template("index.html", result=result, error=None, task=task)

        filename = str(uuid.uuid4()) + "_" + uploaded_file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        uploaded_file.save(filepath)

        # Choose operation
        if task == "hash":
            result = hasher.generate_hashes_web(filepath)
        elif task == "meta":
            result = metadata_extractor.extract_metadata_web(filepath)
        elif task == "timeline":
            result = timeline.get_file_timeline_web(filepath)
        elif task == "scan":
            # If zip uploaded, extract first
            if filename.endswith(".zip"):
                extract_path = os.path.join(UPLOAD_FOLDER, filename + "_unzipped")
                with zipfile.ZipFile(filepath, "r") as zip_ref:
                    zip_ref.extractall(extract_path)
                result = dir_scanner.scan_directory_web(extract_path)
            else:
                result = {"error": "Scan requires ZIP of a directory."}

    return render_template("index.html", result=result)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(os.path.join(REPORT_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

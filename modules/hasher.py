import hashlib # For hashing algorithms
import os # For file system checks

def generate_hashes_web(file_path):
    if not os.path.isfile(file_path):
        return {"error": "File not found."}

    with open(file_path, "rb") as f:
        file_data = f.read()

    return {
        "MD5": hashlib.md5(file_data).hexdigest(),
        "SHA1": hashlib.sha1(file_data).hexdigest(),
        "SHA256": hashlib.sha256(file_data).hexdigest(),
    }

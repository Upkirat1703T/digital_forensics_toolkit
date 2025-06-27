# Digital Forensics Toolkit

A lightweight, modular command-line and web-based tool for digital forensic investigations, including file hashing, metadata extraction, timeline generation, and directory scanning.

---

## Features

- Compute multiple cryptographic hashes (MD5, SHA1, SHA256) of files
- Extract file and image metadata (EXIF, document properties)
- Generate file timeline information (creation, modification, access)
- Scan directories for forensic artifacts and generate JSON/CSV reports
- Web interface for easy upload, analysis, and report downloads

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/digital-forensics-toolkit.git
   cd digital-forensics-toolkit
2. Create a virtual environment

   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
   pip install -r requirements.txt
## Usage
   python app.py
   Open your browser and visit http://127.0.0.1:5000 to use the web interface.

##Contributions 
   Contributions, issues, and feature requests are welcome! Feel free to open a pull request or issue.
## License
   This project is licensed under the MIT License.
## Contact
   Created by Upkirat Singh Dhillon - upkirats05@gmail.com
   
---

### requirements.txt
Flask==2.3.2
PyPDF2==3.0.1
python-docx==0.8.11
Pillow==10.0.0
flask-login==0.6.2

*(You can generate this by running `pip freeze > requirements.txt` in your environment.)*

---

### Procfile

web: python app.py


---

### app.py snippet for deployment compatibility

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

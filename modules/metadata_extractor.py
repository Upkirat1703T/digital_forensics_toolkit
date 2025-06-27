import os
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata_web(file_path):
    if not os.path.isfile(file_path):
        return {"error": "File not found."}

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_pdf_metadata_web(file_path)
    elif ext == ".docx":
        return extract_docx_metadata_web(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".tiff"]:
        return extract_image_metadata_web(file_path)
    else:
        return {"error": f"Unsupported file type: {ext}"}

def extract_pdf_metadata_web(file_path):
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        info = reader.metadata
        return {key: str(value) for key, value in info.items()}
    except Exception as e:
        return {"error": f"PDF metadata extraction error: {e}"}

def extract_docx_metadata_web(file_path):
    try:
        from docx import Document
        doc = Document(file_path)
        props = doc.core_properties
        return {
            "Author": props.author,
            "Title": props.title,
            "Created": str(props.created),
            "Modified": str(props.modified),
            "Last Modified By": props.last_modified_by
        }
    except Exception as e:
        return {"error": f"DOCX metadata extraction error: {e}"}

def extract_image_metadata_web(file_path):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS

        image = Image.open(file_path)
        info = image._getexif()
        if not info:
            return {"info": "No EXIF data found."}

        # Convert all values to strings for JSON serialization
        exif_data = {}
        for tag, value in info.items():
            key = TAGS.get(tag, tag)
            exif_data[key] = str(value)  # convert value to string

        return exif_data

    except Exception as e:
        return {"error": f"Image metadata extraction error: {e}"}

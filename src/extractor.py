import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(path: str) -> str:
    text = ""
    with fitz.open(path) as pdf:
        for page in pdf:
            text += page.get_text("text")
    return text

def extract_text_from_docx(path: str) -> str:
    doc = docx.Document(path)
    return "
".join([p.text for p in doc.paragraphs])

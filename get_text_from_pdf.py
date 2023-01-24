# External Python Modules
from PyPDF2 import PdfReader

# Parameters 
PDF_FILE = "data/test.pdf"
reader = PdfReader(PDF_FILE)
sep = "-" * 20

print(sep, "Text content of first page", sep )
page = reader.pages[0]
print(page.extract_text())

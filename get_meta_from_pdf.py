# External Python Modules
from PyPDF2 import PdfReader

# Parameters 
PDF_FILE = "data/test.pdf"
reader = PdfReader(PDF_FILE)
sep = "-" * 20

print(sep, "Number of pages", sep)
# Extracting number of pages
number_of_pages = len(reader.pages)
print(f"Number of pages: {number_of_pages}")

print(sep, "Predefined Metadata", sep)
# Extracting meta-data. Note that all/a lot could be None
meta = reader.metadata
print(f"Author: {meta.author}")
print(f"Creator: {meta.creator}")
print(f"Producer: {meta.producer}")
print(f"Subject: {meta.subject}")
print(f"Title: {meta.title}")

print(sep, "All metadata found", sep)
print(f"All: {meta}")
for (tag_name, tag_value) in meta.items():
    print (f"{tag_name.strip('/')}: {tag_value} ({type(tag_value)})")

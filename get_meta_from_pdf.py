# -*- coding: utf-8 -*-
__author__ = 'P. Saint-Amand'
__appname__ = 'extract_from_pdf'
__version__ = 'V 0.0.1'

# External Python Modules
from PyPDF2 import PdfReader

# Parameters 
PDF_FILE = "data/test.pdf"
reader = PdfReader(PDF_FILE)

print("-" * 15, "Number of pages", "-" * 15 )
# Extracting number of pages
number_of_pages = len(reader.pages)
print(f"Number of pages: {number_of_pages}")

print("-" * 15, "Metadata", "-" * 15 )
# Extracting nmeta-data. Note that all/a lot could be None
meta = reader.metadata
print(f"Author: {meta.author}")
print(f"Creator: {meta.creator}")
print(f"Producer: {meta.producer}")
print(f"Subject: {meta.subject}")
print(f"Title: {meta.title}")

print("-" * 15, "Text content of first page", "-" * 15 )
page = reader.pages[0]
print(page.extract_text())

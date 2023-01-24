# External Python Modules
import re
from PyPDF2 import PdfReader

# Parameters 
PDF_FILE = "data/test.pdf"
PDF_FILE = "data/ascencio_rapportannuel2021_a4_fr.pdf"
reader = PdfReader(PDF_FILE)
sep = "-" * 20
email_extract_pattern = "(?!\.)[\w\-_.]*[^.]@\w+\.\w+"


all_emails={}     # Dictionary of set (dictionary : {list of pages wher found})
print(sep, f"Extracting emails on all pages (#{len(reader.pages)})", sep)
for i, page in enumerate(reader.pages):
    urls = re.findall(email_extract_pattern, page.extract_text())
    for url in urls:
        if url not in all_emails:
            all_emails[url]=set()
        all_emails[url].add(i+1)
print(all_emails)
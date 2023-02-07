from  PyPDF2 import PdfFileReader

pdf_file_name = 'Project pdf.pdf'
with open(pdf_file_name, 'rb') as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    page_nums = pdf_reader.numpages
    for page_num in range(page_nums):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        print(text)

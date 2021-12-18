
from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)


def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i).rotateClockwise(90))

    with open('./Output/rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)


def merge_pdfs(pathA, pathB):
    pdf_writer = PdfFileWriter()

    pdf_reader = PdfFileReader(pathA)
    for page in range(pdf_reader.getNumPages()):
        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_reader = PdfFileReader(pathB)
    for page in range(pdf_reader.getNumPages()):
        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open('./Output/merged_pages.pdf', 'wb') as out:
        pdf_writer.write(out)


def pdf_split(path, ranges):
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()

    for page in range(int(ranges)):
        pdf_writer.addPage(pdf.getPage(page))
    with open('./Output/SplitA.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    pdf_writer = PdfFileWriter()
    for page in range(int(ranges), pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    with open('./Output/SplitB.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)


def create_watermark(input_pdf, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open('./Output/Watermarked.pdf', 'wb') as out:
        pdf_writer.write(out)


def add_encryption(input_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    with open('./Output/Encrypted.pdf', 'wb') as fh:
        pdf_writer.write(fh)

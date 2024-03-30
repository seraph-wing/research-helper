"""
This file is to create a dataloader for pdf files, given a pdf file, the output should be a list of strings, each string is a paragraph in the pdf file.
"""

import unstructured 


class PDFDataIngestor:
    """
    This class is to create a dataloader for pdf files, given a pdf file, the output should be a list of strings, each string is a paragraph in the pdf file.
    """
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.pdf_text = unstructured.read_pdf(pdf_file_path)
        
    
    def get_paragraphs(self):
        self.paragraphs = unstructured.extract_paragraphs(self.pdf_text)
        return self.paragraphs
    
    def get_abstract(self):
        # return unstructured.extract_abstract(self.pdf_text)
        pass
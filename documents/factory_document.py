from __future__ import annotations
from documents.document import Document
from documents.pdf_document import PDFDocument
from documents.docx_document import DOCXDocument


class Creator:

    @classmethod
    def create(cls, path_to_file: str, user_id: str, primary: bool = False) -> Document:
        if path_to_file.endswith('.pdf'):
            return PDFDocument(user_id, path_to_file, primary)
        if path_to_file.endswith('.docx'):
            return DOCXDocument(user_id, path_to_file, primary)
        raise ValueError(f'Invalid extension with file: {path_to_file}')

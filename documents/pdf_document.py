import pdfrw
from documents.document import Document
from documents.logging_dir import logging_decorators
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt

class PDFDocument(Document):
        
    def extract_text(self) -> str:
            with open(self.path, 'rb') as pdf_file:
                read_pdf = pdfrw.PdfReader(pdf_file)
                number_of_pages = len(read_pdf.pages)
                text = ''
                for i in range(number_of_pages):
                    page = read_pdf.pages[i]
                    if page is not None:
                        page_content = page.extract_text()
                        if page_content:
                            text += page_content
            return text


    def set_up_meta(self, control_sum: str):
        writer = pdfrw.PdfWriter()
        for page in pdfrw.PdfReader(self.path).pages:
            writer.add_page(page)
        writer.trailer.Info = pdfrw.IndirectPdfDict(
            Owner=self.user_id,
            ControlSum=control_sum,
            SignedBy=''
        )
        writer.write(self.path)

    def set_up_file(self):
        text = self.extract_text()
        control_sum = self.get_control_sum(text)
        trailer = pdfrw.PdfReader(self.path)
        try:
            trailer.Info.Owner = self.user_id
            trailer.Info.ControlSum = control_sum
            trailer.Info.SignedBy = ''
            pdfrw.PdfWriter(self.path, trailer=trailer).write()
        except AttributeError:
            self.set_up_meta(control_sum)
        self.primary = False

    def is_signed_by(self) -> bool:
        return self.user_id in self.who_signed()

    @logging_decorators.sign_logger
    def sign(self):
        trailer = pdfrw.PdfReader(self.path)
        if self.validate():
            signed_by = ' '.join(self.who_signed() + [self.user_id])
            trailer.Info.SignedBy = signed_by
        pdfrw.PdfWriter(self.path, trailer=trailer).write()

    def validate(self) -> bool:
        trailer = pdfrw.PdfReader(self.path)
        if not (trailer.Info and trailer.Info.ControlSum):
            raise ValueError('Document has never been initialized')
        control_sum = str(trailer.Info.ControlSum)
        if self.get_control_sum(self.extract_text()) == control_sum[1:len(control_sum) - 1]:
            return True
        raise ValueError('Document has been changed. Control sum does not match the content')

    def who_signed(self) -> list[str]:
        trailer = pdfrw.PdfReader(self.path)
        signed_by = trailer.Info.SignedBy
        return signed_by[1:len(signed_by) - 1].split()

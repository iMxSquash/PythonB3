from ..mixins.PrintableMixin import PrintableMixin
from .Document import Document

class PdfDocument(Document, PrintableMixin):
    def __init__(self, title: str, content: str, page_count: int):
        super().__init__(title, content, type="PDF")
        self.page_count = page_count
from ..mixins.PrintableMixin import PrintableMixin
from .Document import Document

class WordDocument(Document, PrintableMixin):
    def __init__(self, title: str, content: str, word_count: int):
        super().__init__(title, content, type="Word")
        self.word_count = word_count
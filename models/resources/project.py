import uuid

from sqlalchemy import Column, String, DateTime, ColumnElement

from models.base import Base
from nguylinc_python_utils.sqlalchemy import BaseExtended


class Project(Base, BaseExtended):
    __tablename__ = "projects"
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(100), index=True, unique=True)
    created_at: ColumnElement = Column(DateTime(), index=True)
    updated_at: ColumnElement = Column(DateTime(), index=True)
    editable_fields = ["name"]

    def get_pdf_location(self):
        return f"{self.name}/book.pdf"

    def get_word_list_location(self):
        return f"{self.name}/word_list.xlsx"

    def get_book_index_location(self):
        return f"{self.name}/book_index.xlsx"

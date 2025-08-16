# src/models/content.py
from pydantic import BaseModel
from typing import List, Optional

class PdfDoc(BaseModel):
    id: str                   # hash/url id
    title: str
    url: str
    source: str               # 'NCERT'/'CBSE'/'SEBA'/'AHSEC'/'UGC' etc.
    class_level: str          # '6'...'12','degree'
    subject: str
    language: str             # 'as','hi','en'
    cached_file_id: Optional[str] = None   # Telegram file_id cache

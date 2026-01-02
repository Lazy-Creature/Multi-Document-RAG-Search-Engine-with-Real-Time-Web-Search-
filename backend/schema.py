from dataclasses import dataclass
from typing import Dict

@dataclass
class Document:
    source_id:str
    source_type:str
    title:str
    content:str
    metadata:Dict

@dataclass
class WebSearchResult:
    title:str
    url:str
    content:str

@dataclass
class AnswerSource:
    label:str
    content:str

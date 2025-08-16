# Simple extractive summary from PDF text using TextRank (sumy)
from io import BytesIO
from pdfminer.high_level import extract_text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import requests


def summarize_pdf_url(pdf_url: str, sentences: int = 5):
    pdf_bytes = requests.get(pdf_url, timeout=60).content
    text = extract_text(BytesIO(pdf_bytes))
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    sents = summarizer(parser.document, sentences)
    return "\n".join([str(s) for s in sents])

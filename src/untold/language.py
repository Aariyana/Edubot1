from langdetect import detect

def auto_detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

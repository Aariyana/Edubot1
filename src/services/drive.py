import requests
import os

API_KEY = os.getenv("GOOGLE_DRIVE_API_KEY")

# For public files only; premium users get direct file via Telegram

def get_public_file_metadata(file_id: str):
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}"
    r = requests.get(url, params={"key": API_KEY, "fields": "id,name,mimeType,size,webViewLink,webContentLink"}, timeout=30)
    r.raise_for_status()
    return r.json()

import os, requests

CSE_ID = os.getenv("GOOGLE_CSE_ID")
CSE_KEY = os.getenv("GOOGLE_CSE_KEY")

DEFAULT_SITES = [
  "ncert.nic.in",          # NCERT textbooks, exemplar
  "cbseacademic.nic.in",  # CBSE curriculum
  "sebaonline.org",       # Assam board
  "ahsec.assam.gov.in",   # Assam Higher Secondary
  "ugc.ac.in",            # UGC model curriculum
]

# Build a query like: class 6 math syllabus site:ncert.nic.in filetype:pdf

def search_pdfs(query: str, sites=DEFAULT_SITES, num=5):
    site_filter = " OR ".join([f"site:{s}" for s in sites])
    q = f"{query} ({site_filter}) filetype:pdf"
    resp = requests.get("https://www.googleapis.com/customsearch/v1", params={
        "key": CSE_KEY,
        "cx": CSE_ID,
        "q": q,
        "num": num,
    }, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("items", []):
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "displayLink": item.get("displayLink"),
        })
    return results

import os
import requests

CSE_ID = os.getenv("GOOGLE_CSE_ID")
CSE_KEY = os.getenv("GOOGLE_CSE_KEY")

def search_pdfs(query: str, num=5):
    try:
        if not CSE_ID or not CSE_KEY:
            raise ValueError("Google CSE API credentials not configured")
        
        # Build query with filetype filter
        search_query = f"{query} filetype:pdf"
        
        # Make API request
        response = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params={
                "key": CSE_KEY,
                "cx": CSE_ID,
                "q": search_query,
                "num": num,
                "safe": "active"  # Safe search
            },
            timeout=30
        )
        
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get("items", []):
            # Only include PDF results
            if item.get("link", "").endswith('.pdf'):
                results.append({
                    "title": item.get("title", "No title"),
                    "link": item.get("link"),
                    "displayLink": item.get("displayLink", "Unknown source")
                })
        
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"API Request error: {e}")
        return []
    except ValueError as e:
        print(f"Configuration error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
STRINGS = {
  "en": {
    "start": "Hi {name}! I’m EduBot. Use /pdf, /question, /quiz, /referral, /profile.",
    "premium_needed": "Premium needed. Watch 40s ad on site or use referral to get 1 day premium.",
  },
  "hi": {
    "start": "नमस्ते {name}! EduBot में आपका स्वागत है. /pdf, /question, /quiz…",
    "premium_needed": "प्रीमियम चाहिए. साइट पर 40 सेकंड का ऐड देखें या रेफरल से 1 दिन प्रीमियम पाएँ.",
  },
  "as": {
    "start": "নমস্কাৰ {name}! মই EduBot. /pdf, /question, /quiz, /referral, /profile ব্যৱহাৰ কৰক.",
    "premium_needed": "প্ৰিমিয়াম দরকাৰ। ছাইটত ৪০ ছেকেণ্ড এড চাওঁক বা ৰেফাৰেলৰে ১ দিনৰ প্ৰিমিয়াম পাওঁক.",
  }
}

def t(lang: str, key: str, **kwargs):
    d = STRINGS.get(lang or "en", STRINGS["en"])
    return d.get(key, key).format(**kwargs)

# src/models/user.py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    tg_id: int
    name: Optional[str] = None
    lang: str = "en"               # 'as', 'hi', 'en'
    is_premium: bool = False
    premium_until: Optional[datetime] = None
    referrals: List[int] = []        # tg_ids of referred users
    referral_code: str
    referred_by: Optional[int] = None
    reward_points: int = 0
    daily_pdf_count: int = 0
    daily_pdf_date: Optional[str] = None  # YYYY-MM-DD

from aiogram import types, Router
from datetime import datetime, timedelta
from src.db import users_col

router = Router()

@router.message(commands=["referral"])
async def referral_cmd(msg: types.Message):
    """Show referral link + referral stats"""
    tg_id = msg.from_user.id
    user = users_col.find_one({"tg_id": tg_id})
    if not user:
        await msg.answer("⚠️ Please use /start first.")
        return
    
    referral_link = f"https://t.me/{(await msg.bot.get_me()).username}?start={user['referral_code']}"
    count = len(user.get("referrals", []))
    reward_points = user.get("reward_points", 0)
    
    await msg.answer(
        f"🎁 Invite your friends!\n\n"
        f"🔗 Your referral link:\n{referral_link}\n\n"
        f"👥 Referrals: {count}\n"
        f"⭐ Reward Points: {reward_points}\n"
        f"⚡ Rule: Every 10 referrals = +3 hours Premium"
    )


@router.message(commands=["start"])
async def start_cmd(msg: types.Message):
    """Start command with referral support"""
    args = msg.text.split()
    tg_id = msg.from_user.id
    name = msg.from_user.full_name

    user = users_col.find_one({"tg_id": tg_id})

    if not user:
        referred_by = None
        if len(args) > 1:
            referral_code = args[1]
            ref_user = users_col.find_one({"referral_code": referral_code})
            if ref_user and ref_user["tg_id"] != tg_id:
                referred_by = ref_user["tg_id"]

                # Get current referral count
                new_count = len(ref_user.get("referrals", [])) + 1
                update_data = {
                    "$push": {"referrals": tg_id},
                    "$inc": {"reward_points": 10}  # Optional: add reward points
                }

                # ✅ Every 10 referrals → +3 hours Premium
                if new_count % 10 == 0:
                    premium_until = ref_user.get("premium_until")
                    if premium_until and premium_until > datetime.utcnow():
                        premium_until += timedelta(hours=3)
                    else:
                        premium_until = datetime.utcnow() + timedelta(hours=3)
                    update_data["$set"] = {
                        "is_premium": True,
                        "premium_until": premium_until
                    }

                users_col.update_one({"tg_id": ref_user["tg_id"]}, update_data)

        # Create new user
        users_col.insert_one({
            "tg_id": tg_id,
            "name": name,
            "lang": "en",
            "is_premium": False,
            "premium_until": None,
            "referrals": [],
            "referral_code": str(tg_id),
            "referred_by": referred_by,
            "reward_points": 0,
            "daily_pdf_count": 0,
            "daily_pdf_date": None,
            "created_at": datetime.utcnow()
        })
        await msg.answer(f"👋 Hello {name}! Your account has been created ✅")
    else:
        await msg.answer(f"Welcome back, {name}! 🎓")

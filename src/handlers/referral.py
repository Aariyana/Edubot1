from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from ..db import users, referrals
import secrets
from datetime import datetime, timedelta

router = Router()

@router.message(Command("referral"))
async def referral(m: Message):
    uid = m.from_user.id
    u = await users.find_one({"tg_id": uid})
    if not u:
        await m.answer("Please send /start first.")
        return

    # ensure referral code exists
    if not u.get("ref_code"):
        code = secrets.token_urlsafe(6)
        await users.update_one({"tg_id": uid}, {"$set": {"ref_code": code}})
        u["ref_code"] = code

    link = f"https://t.me/{(await m.bot.me()).username}?start={u['ref_code']}"
    await m.answer(
        "<b>Referral Program</b>\n"
        "🔗 Share this link and get rewards!\n"
        f"{link}\n\n"
        "• প্রত্যেক সফল ১জন ৰেফাৰ = ১ পইন্ট\n"
        "• ১০ জন ৰেফাৰ = ৪ ঘণ্টা ফ্ৰী প্ৰিমিয়াম"
    )

@router.message(Command("start"))
async def start_with_code(m: Message):
    # This overlaps with start.py, but here we catch ?start=<code> deep-link
    if not m.text or " " not in m.text:
        return
    arg = m.text.split(" ", 1)[1].strip()
    if not arg:
        return

    me_id = m.from_user.id
    inviter = await users.find_one({"ref_code": arg})
    if not inviter or inviter.get("tg_id") == me_id:
        return  # invalid/self

    # Check if this user is new referral (first time)
    already = await referrals.find_one({"invitee": me_id})
    if already:
        return

    await referrals.insert_one({
        "inviter": inviter["tg_id"],
        "invitee": me_id,
        "at": datetime.utcnow()
    })

    # Add point
    await users.update_one({"tg_id": inviter["tg_id"]}, {"$inc": {"points": 1}})

    # If reached 10, give 4 hours premium
    inv_user = await users.find_one({"tg_id": inviter["tg_id"]})
    pts = int(inv_user.get("points", 0))
    if pts % 10 == 0:  # every 10 points
        until = datetime.utcnow() + timedelta(hours=4)
        await users.update_one(
            {"tg_id": inviter["tg_id"]},
            {"$set": {"is_premium": True, "premium_until": until}}
        )
        await m.bot.send_message(inviter["tg_id"], "🎉 You reached 10 referrals! 4 hours premium unlocked.")
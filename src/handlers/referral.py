from datetime import datetime, timedelta

# ... inside start command while updating referrer ...
new_count = len(ref_user.get("referrals", [])) + 1
update_data = {"$push": {"referrals": tg_id}}

# ✅ Every 10 referrals = 3 hours premium
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

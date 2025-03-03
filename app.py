import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# 🔹 আপনার Telegram Bot Token
TOKEN = "7669153355:AAHFQrk5U6Uqno-i4v166VRMwdN34fsq8Kk"

# ✅ ইউজারের মেসেজের রিপ্লাই ফাংশন (async method)
async def handle_message(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"🤖 আপনি বললেন: {text}")

# ✅ অ্যাপ তৈরি করা
app = Application.builder().token(TOKEN).build()

# 🔹 মেসেজ হ্যান্ডলার যোগ করা
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# ✅ বট চালানো (asyncio loop)
async def main():
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())

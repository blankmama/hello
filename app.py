from flask import Flask, request
import telegram
import os

# Telegram Bot Token (Railway-এর Environment Variable থেকে)
TOKEN = os.getenv("BOT_TOKEN")  
bot = telegram.Bot(token=TOKEN)

# Flask অ্যাপ তৈরি
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    """ টেলিগ্রাম বটের জন্য Webhook হ্যান্ডলার """
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # ইউজারকে রিপ্লাই পাঠানো
    bot.send_message(chat_id=chat_id, text=f"🤖 আপনি বললেন: {text}")

    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    """ হোমপেজ টেস্টিং """
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(port=5000)

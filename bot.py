from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# আপনার টোকেন এখানে বসান
TOKEN = '7669153355:AAHFQrk5U6Uqno-i4v166VRMwdN34fsq8Kk'

async def start(update: Update, context):
    await update.message.reply_text('হাই')

async def echo(update: Update, context):
    await update.message.reply_text('হাই')

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # কমান্ড হ্যান্ডলার
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # মেসেজ হ্যান্ডলার
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    # বট চালু করুন
    application.run_polling()

if __name__ == '__main__':
    main()

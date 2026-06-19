from telegram import Bot
from config import BOT_TOKEN, CHANNELS

bot = Bot(token=BOT_TOKEN)

def send_product(text, source):
    # القناة الخاصة بالمصدر
    if source == "aliexpress":
        bot.send_message(CHANNELS["aliexpress"], text)
    elif source == "shein":
        bot.send_message(CHANNELS["shein"], text)
    elif source == "amazon":
        bot.send_message(CHANNELS["amazon"], text)

    # القناة العامة دائمًا
    bot.send_message(CHANNELS["@pick2takecom"], text)
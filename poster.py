from telegram import Bot
from config import BOT_TOKEN, CHANNELS

bot = Bot(token=1751962838:AAEJxl4gm9-ytzpvGlJa53ddFEsstBJ_kS8)

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

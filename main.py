import time
from aliexpress import get_products
from poster import send_product

def format_product(p):
    return f"""
🔥 عرض جديد

🛍️ {p['title']}
💰 السعر: {p['price']}

🔗 اشتر الآن:
{p['link']}
"""

def run():
    while True:
        products = get_products()

        for p in products:
            text = format_product(p)
            send_product(text, "aliexpress")

        print("Posted batch...")
        time.sleep(3600)  # كل ساعة

if __name__ == "__main__":
    run()
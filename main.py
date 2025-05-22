print("Запуск main.py")

import time
from config import KIJIJI_SEARCH_URLS, CHECK_INTERVAL
from kijiji_parser import get_kijiji_ads
from telegram_bot import send_message

def load_sent_ads():
    try:
        with open('sent_ads.txt', 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        print("Файл sent_ads.txt не найден. Создаю новый список.")
        return set()

def save_sent_ad(url):
    with open('sent_ads.txt', 'a') as f:
        f.write(url + '\n')

def main():
    print("main() запущен.")
    sent_ads = load_sent_ads()

    while True:
        try:
            for url in KIJIJI_SEARCH_URLS:
                print(f"Проверяю: {url}")
                ads = get_kijiji_ads(url)
                print(f"Объявлений найдено: {len(ads)}")
                for title, ad_url in ads:
                    if ad_url not in sent_ads:
                        print(f"Новое объявление:\n{title}\n{ad_url}")
                        send_message(f"🔔 Новое объявление:\n{title}\n{ad_url}")
                        save_sent_ad(ad_url)
                        sent_ads.add(ad_url)
            print(f"Пауза {CHECK_INTERVAL} сек...")
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print(f"[ОШИБКА в main]: {e}")
            time.sleep(60)

if __name__ == '__main__':
    main()
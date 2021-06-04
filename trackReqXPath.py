from lxml import html
import requests
import datetime
import threading
import time
import winsound

# format: title, url, xpath, non alarm value
SITE_DATA_LST = [
    ('3060 Ti BestBuy',
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402',
    '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    'Sold Out'),
    ('3070    BestBuy',
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442',
    '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    'Sold Out'),
    # ('3070 Ti BestBuy',
    # 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789',
    # '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    # 'Coming Soon'),
    ('3080    BestBuy',
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    'Sold Out'),
    ('3080 Ti BestBuy',
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956',
    '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    'Sold Out'),
    ('3090    BestBuy',
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434',
    '/html/body/div/main/div/div/div/div/div/div/div/div/div/div/button/text()',
    'Sold Out')
    # ('mangaupdates release 1st',
    # 'https://www.mangaupdates.com/releases.html',
    # '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/a/text()',
    # 'Doujima-Kun Won\'t Be Disturbedd')
]
FIREFOX_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
ALARM_BEEP_DURATION = 1000  # milliseconds
ALARM_FREQ = 440  # Hz
ALARM_DURATION = 60  # 2n sec
SLEEP_SCRAPE_DUR = 60  # sec
ALARM_ON = False

def alarm(run_event):
    global ALARM_ON
    for _ in range(ALARM_DURATION):
        if not run_event.is_set():
            break
        winsound.Beep(ALARM_FREQ, ALARM_BEEP_DURATION)
        time.sleep(1)
    ALARM_ON = False

def main():
    # ALARM_ON = False
    global ALARM_ON

    run_event = threading.Event()
    run_event.set()

    try:
        while True:
            for site_data in SITE_DATA_LST:
                try:
                    page = requests.get(site_data[1], headers=FIREFOX_HEADER)
                    tree = html.fromstring(page.content)
                    ele_lst = tree.xpath(site_data[2])
                except requests.exceptions.RequestException as e:
                    print("requests.get exception: ")
                    print(e)
                    ele_lst = ['REQUESTS.GET_EXCEPTION']
                if ele_lst:
                    element = ele_lst[0]
                else:
                    element = 'EMPTY_ELE_LIST'
                print(f'{site_data[0]} | {element} | {datetime.datetime.now()} | {ele_lst}')

                if element != site_data[3]:
                    print('*** ALARM VALUE ABOVE ***')
                if element != site_data[3] and not ALARM_ON:
                    ALARM_ON = True
                    print('*** ALARM TRIGGERED ***')
                    alarm_thread = threading.Thread(target=alarm, args=(run_event,))
                    alarm_thread.start()
            
            print('---sleeping---')
            time.sleep(SLEEP_SCRAPE_DUR)
    except KeyboardInterrupt:
        print('attempting to close threads')
        run_event.clear()

if __name__ == "__main__":
    main()

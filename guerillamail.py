#GuerillaMail Scrape
try:
    from selenium import webdriver as wd
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
except:
    print('[x] Selenium not installed, run the following command to install selenium!')
    print('sudo pip3 install selenium')

from random import randint
import time

proxylist = [
    '190.152.213.126:38855',
    '61.8.66.178:8080',
    '1.20.103.58:49033',
    '90.182.164.122:54193',
    '95.0.226.84:42388',
    '180.180.218.227:53730',
    '118.174.220.49:35997',
    '125.27.251.248:56951',
    '103.50.6.53:35977',
    '210.11.181.221:55331',
    '75.98.119.13:57859',
    '208.97.119.150:55794',
    '178.134.152.46:41054',
    '118.174.220.61:47405',
    '36.67.212.161:37672',
    '165.227.210.53:3128',
    '182.53.206.155:34307',
    '36.37.112.6:47527'
]


def main():
    url = 'https://www.guerrillamail.com/'

    r = randint(0, len(proxylist)-1)
    myProxy = proxylist[r]

    proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    })


    options = Options()
    options.headless = True

    driver = wd.Firefox(options=options, proxy=proxy)
    driver.get(url)

    email = driver.find_element_by_xpath('//*[@id="inbox-id"]').text+'@'+driver.find_element_by_xpath('//*[@id="gm-host-select"]').text.split('\n')[0]
    mail = driver.find_elements_by_xpath('//*[contains(@class, "mail_row")]')
    print('[-] Waiting for mail', (email))
    while True:
        if len(mail) == 1:
            time.sleep(10)
            mail = driver.find_elements_by_xpath('//*[contains(@class, "mail_row")]')
        else:
            print('[-] You\'ve got mail!')

            for item in mail:
                driver.refresh()
                print('-'*20)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "mail_row")]')))
                link = driver.find_element_by_xpath('//*[contains(@id, "mr_")]/td[3]/a')
                link.click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "email_body")]')))
                body = driver.find_element_by_xpath('//*[contains(@class, "email_body")]').text
                print(body)
                print('-'*20)
                back = driver.find_element_by_xpath('//*[@id="back_to_inbox_link"]')

                back.click()
                return

    print(email)

if __name__ == '__main__':
    main()

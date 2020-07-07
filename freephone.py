# Make sure you have selenium and firefox installed as well as the geckodriver executable, found at the link below:
# https://github.com/mozilla/geckodriver/releases

# Tested on Python2.7 because Python3 is lame.
# Will probably work pretty easily on 3 tho.

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

import time

def main():

        # Enter the url of the site with free phone numbers 
        og_url = 'https://receive-sms.cc/US-Phone-Number/'
        
        options = Options()
        options.headless = True
        
        expath = r'ENTER PATH TO GECKODRIVER HERE'

        driver = wd.Firefox(options=options,executable_path=expath)
        driver.get(og_url)
        
        # This is the xpath of the HTML object that holds the phone number. It's relatively trivial to do this on any web page. 
        # Google "extract xpath for selenium" or something like that to figure it out. Basically, you just need the class name or the
        # id of the HTML object.
        nums = driver.find_elements_by_xpath('//*[@class="number-boxes-item-number"]')
        # This is the addition to the initial URL that you can use to go through pages. 
        link_page_addition = 'Page/'
        
        numarr = []

        index = 1
        print('[-] Page 1:')
        for item in nums:
                numarr.append(item.text.split(' ')[1])
                print('\t'+item.text.split(' ')[1])

        while index <= 10:
                print('[-] Page '+str(index))
                url = og_url+link_page_addition+str(index)
                driver.get(url)

                nums = driver.find_elements_by_xpath('//*[@class="number-boxes-item-number"]')

                for item in nums:
                        numarr.append(item.text.split(' ')[1])
                        print('\t'+item.text.split(' ')[1])
                index+=1
                # Please leave this in here. The people who offer the free SMS service deserve to keep their service up. There's no point in DoS'ing them so
                # you can run this script faster. If anything, increase it. I'm not responsible for you being an asshole.
                time.sleep(10)

if __name__ == '__main__':
        main()

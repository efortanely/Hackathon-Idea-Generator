import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initialize_browser(debug_mode):
    options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    options.add_experimental_option('prefs', prefs)
    if not debug_mode:
        options.add_argument('headless')

    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
    browser.set_page_load_timeout(100)
    browser.get('https://devpost.com/software/trending')
    return browser


def inspect_hacks(browser, hacks_data, num_hacks=2500):
    page_num = 1
    hacks = 0
    
    while hacks < num_hacks:
        hacks_class = 'block-wrapper-link.fade.link-to-software'
        hacks_on_page = browser.find_elements_by_class_name(hacks_class)

        for i in range(len(hacks_on_page)):
            hacks_on_page = browser.find_elements_by_class_name(hacks_class)
            
            if hacks >= num_hacks:
                break
            
            hack = hacks_on_page[i]
            title_class = 'software-entry-name.entry-body'
            hack_title = hack.find_element_by_class_name(title_class).text
            hack_token = hack_title.lower().split()[0]
            hack.click()
            wait = WebDriverWait(browser, 20)
            
            try:
                wait.until(EC.url_contains(hack_token))
            except:
                pass

            try:
                info_class = 'large-9.columns'
                info = browser.find_element_by_class_name(info_class).text
                if info:
                    hacks_data.write(info + '\n\n\n')
                    hacks += 1

            except:
                pass

            browser.back()
            wait = WebDriverWait(browser, 20)
            wait.until(EC.url_contains('software/trending'))
        
        page_num += 1
        buttons = browser.find_element_by_class_name('pagination')
        next = buttons.find_element_by_link_text(str(page_num))
        if(next):
            next.click()


hacks_data = open('hacks.txt', 'w')
browser = initialize_browser(debug_mode=False)
inspect_hacks(browser, hacks_data)
hacks_data.close()
browser.close()
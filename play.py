#!/usr/bin/python
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()
#browser.close()
#quit()
#pkill -f firefox to kill all processes!
#!/usr/bin/python
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('http://wecsfm.com')
browser.find_element_by_xpath('//*[@title="play"').click()
#browser.close()
#quit()
#pkill -f firefox to kill all processes!
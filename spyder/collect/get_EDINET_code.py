import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

url = "https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.bean=ee.bean.W1E62071.EEW1E62071Bean&uji.verb=W1E62071InitDisplay&TID=W1E62071&PID=W0EZ0001&SESSIONKEY=&lgKbn=2&dflg=0&iflg=0"

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
    options = options
)

# url = "https://www.google.co.jp/"
driver.get(url)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')

#HTMLファイルとして保存したい場合はファイルオープンして保存
with open('EDINET.html', mode='w', encoding = 'utf-8') as fw:
    fw.write(soup.prettify())

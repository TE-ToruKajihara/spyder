import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

url = "https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.bean=ee.bean.W1E62071.EEW1E62071Bean&uji.verb=W1E62071InitDisplay&TID=W1E62071&PID=W0EZ0001&SESSIONKEY=&lgKbn=2&dflg=0&iflg=0"


driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)

# url = "https://www.google.co.jp/"
driver.get(url)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')

#HTMLファイルとして保存したい場合はファイルオープンして保存
with open('EDINET.html', mode='w', encoding = 'utf-8') as fw:
    links = soup.find_elements_by_link_tex("javascript:EEW1E62071EdinetCodeListDownloadAction( 'lgKbn=2&amp;dflg=0&amp;iflg=0&amp;dispKbn=1')")
    print(links)
    fw.write(soup.prettify())

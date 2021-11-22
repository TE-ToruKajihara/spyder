import requests
import chardet
from bs4 import BeautifulSoup
import re
import time
import os

#取得系
def get_soup(url):
    #Requestsを使って、webから取得
    r = requests.get(url)
    #要素を抽出
    return BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
    # return BeautifulSoup(r.content, 'html.parser')

def get_link_all(soup):
    return [elem.get('href') for elem in soup.find_all('a')]

def get_csv_all(target_url, save_dir, wait_time = 1):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in get_link_all(get_soup(target_url)):
        file_name, ext = os.path.splitext(os.path.basename(url))
        if ext == '.csv':
            with open(save_dir + file_name + ext, mode='wb') as fw:
                fw.write(requests.get(url).content)
                time.sleep(wait_time)



#保存系
def insert_DB(df, engine, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def save_soup(soup, title = 'originDataOld.html'):
    with open(title, mode='w', encoding = 'utf-8') as fw:
        fw.write(soup.prettify())

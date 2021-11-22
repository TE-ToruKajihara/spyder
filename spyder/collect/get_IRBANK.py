from spyder import *


OUTPUT_DIR = "/home/work/data/IRBANK/"
LAST_YEAR = 2021

#初回のみ
target_url = "https://irbank.net/download"

# #HTMLファイルとして保存したい場合はファイルオープンして保存
# soup = get_soup(target_url)
# save_soup(soup)

#2021年のデータを取得
get_csv_all(target_url, OUTPUT_DIR + str(LAST_YEAR % 100).zfill(4) + "/", 70)

#2010年から2020年のデータを取得    
for year in [str(x % 100).zfill(4) for x in range(2010, LAST_YEAR)]:

    save_dir = OUTPUT_DIR + year + "/"
    get_csv_all(target_url + "/" + year, OUTPUT_DIR + year + "/", 70)

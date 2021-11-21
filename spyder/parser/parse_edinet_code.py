import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text

FILE_PATH = "/home/work/data/input/EdinetcodeDlInfo.csv"
OUTPUT_PATH = "/home/work/data/output/Edinetcode.csv"
TABLE_NAME = "edinet_code_list"

# 接続できているかどうか確認
# print(conn.is_connected())
 

def insert_DB(df, engine, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def csv2df(input_path):
    # ＥＤＩＮＥＴコード,提出者名,証券コードを読み込む（合計3列）
    df = pd.read_csv(FILE_PATH, encoding="cp932", usecols=[0, 6, 11],
                        names=('edinet', 'name', 'security_code'), skiprows=2)

    # 証券コードが欠損値（NaN）である行を削除し証券番号から末尾の0を削除
    df = df.dropna(how='any', axis=0)
    df["security_code"] = df["security_code"].apply(lambda x: x // 10)
    return df


if __name__ == '__main__':

    # コネクションの作成
    conn = mysql.connector.connect(
        host='mysql_db',
        port='3306',
        user='toru',
        password='toru',
        database='mysql_db'
    )

    # コネクションが切れた時に再接続してくれるよう設定
    conn.ping(reconnect=True)
    cursor = conn.cursor()

    engine = create_engine('mysql+mysqlconnector://toru:toru@mysql_db:3306/mysql_db')

    cursor.execute("DROP TABLE IF EXISTS edinet_code_list")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS edinet_code_list (
    edinet CHAR(6) NOT NULL,
    name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci,
    security_code INT(4) NOT NULL PRIMARY KEY
    )""")

    df = csv2df(FILE_PATH)

    insert_DB(df, engine, TABLE_NAME)
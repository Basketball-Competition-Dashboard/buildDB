import csv
import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()

# 讀取CSV檔案並進行欄位名稱對應
with open('csv/game.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    to_db = [(i['game_id'], i['game_date'], i['season_id']) for i in reader]

# 插入數據到SQLite資料表
cursor.executemany("INSERT OR IGNORE INTO Game (GID, Date, SID) VALUES (?,?,?);", to_db)
conn.commit()
conn.close()
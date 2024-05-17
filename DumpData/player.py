import csv
import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()

# 讀取CSV檔案並進行欄位名稱對應
with open('csv/common_player_info.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    to_db = [(i['person_id'], i['first_name'], i['last_name'], i['birthdate'], i['height'], i['weight'], i['position'], i['country'], i['team_id']) for i in reader]

# 插入數據到SQLite資料表
cursor.executemany("INSERT INTO Player (PID, LName, FName, Bdate, Height, Weight, Position, Country, TID) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?);", to_db)
conn.commit()
conn.close()
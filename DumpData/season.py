import csv
import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()

# 讀取CSV檔案並進行欄位名稱對應
with open('csv/game.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [(i['season_id'], int(i['game_date'].split('-')[0])) for i in reader]

# 將資料按照 season_id 分組
grouped_data = {}
for season_id, year in data:
    if season_id in grouped_data:
        grouped_data[season_id].append(year)
    else:
        grouped_data[season_id] = [year]

# 根據分組的資料組合年份範圍
to_db = []
for season_id, years in grouped_data.items():
    min_year = min(years)
    max_year = max(years)
    year_range = f"{min_year}-{max_year}"
    to_db.append((season_id, year_range))

# 插入數據到SQLite資料表
cursor.executemany("INSERT OR IGNORE INTO Season (SID, year) VALUES (?,?);", to_db)
conn.commit()
conn.close()

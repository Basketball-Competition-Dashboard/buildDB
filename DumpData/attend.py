import csv
import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# 讀取CSV檔案並進行欄位名稱對應
with open('csv/line_score.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [(i['game_id'], i['team_id_home'], i['team_id_away'], i['pts_home'], i['pts_away']) for i in reader]

sourceCursor.execute("SELECT line_score.game_id, line_score.team_id_home, line_score.team_id_away, line_score.pts_home, line_score.pts_away from line_score join team on (line_score.team_id_home = team.id or line_score.team_id_away = team.id) join game on line_score.game_id = game.game_id;")
data_to_import = sourceCursor.fetchall()

to_db = []
for gid, team_id_home, team_id_away, score_home, score_away in data_to_import:
    # 將主場隊伍插入到 Attend 表中
    to_db.append((gid, team_id_home, True, score_home))
    # 將客場隊伍插入到 Attend 表中
    to_db.append((gid, team_id_away, False, score_away))

# 插入數據到SQLite資料表
cursor.executemany("INSERT or IGNORE INTO Attend (GID, TID, is_home_team, Score) VALUES (?,?,?,?);", to_db)
conn.commit()
conn.close()
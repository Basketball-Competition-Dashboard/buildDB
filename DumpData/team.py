import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

sourceCursor.execute("select id, full_name, team.city, headcoach, year_founded from team, team_details where team.id = team_details.team_id")
data_to_import = sourceCursor.fetchall()

cursor.executemany("INSERT or IGNORE INTO team ( TID, TName, City, CoachName, YearFounded) Values (?,?,?,?,?)", data_to_import)

# 插入數據到SQLite資料表
conn.commit()
conn.close()
source.close()
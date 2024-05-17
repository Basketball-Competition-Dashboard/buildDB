import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

"""
# player1 Hit 計算並插入
sourceCursor.execute("SELECT game_id, player1_id, count(*) from play_by_play where eventmsgtype = 1 AND eventmsgactiontype = 1 group by game_id,player1_id")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, hit_count = data
    cursor.execute("INSERT OR IGNORE INTO gamerecord (GID, PID, Hit) VALUES (?, ?, ?)", (game_id, player_id, hit_count))
    cursor.execute("UPDATE gamerecord SET Hit = ? WHERE GID = ? AND PID = ?", (hit_count, game_id, player_id))

# player2 Assist 計算並插入
sourceCursor.execute("SELECT game_id, player2_id, count(*) from play_by_play where eventmsgtype = 1 and player2_id != '0' group by game_id,player2_id")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, assist_count = data
    cursor.execute("INSERT OR IGNORE INTO gamerecord (GID, PID, Assist) VALUES (?, ?, ?)", (game_id, player_id, assist_count))
    cursor.execute("UPDATE gamerecord SET Assist = ? WHERE GID = ? AND PID = ?", (assist_count, game_id, player_id))

# player3 Assist計算並插入
sourceCursor.execute("SELECT game_id, player3_id, count(*) from play_by_play where eventmsgtype = 1 and player3_id != '0' group by game_id,player3_id")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, assist_count = data
    cursor.execute("INSERT OR IGNORE INTO gamerecord (GID, PID, Assist) VALUES (?, ?, ?)", (game_id, player_id, assist_count))
    cursor.execute("UPDATE gamerecord SET Assist = ? WHERE GID = ? AND PID = ?", (assist_count, game_id, player_id))
"""

# 計算 3 分球得分
sourceCursor.execute("SELECT game_id, player1_id, count(*)*3 from play_by_play where eventmsgtype = 1 AND eventmsgactiontype = 1 group by game_id,player1_id")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, score = data
    cursor.execute("UPDATE gamerecord SET score = ? WHERE GID = ? AND PID = ?", (score, game_id, player_id))

conn.commit()
conn.close()
source.close()
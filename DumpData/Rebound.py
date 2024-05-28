import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# 計算籃板數
sourceCursor.execute("""
    SELECT game_id, player1_id, count(*)
    FROM play_by_play
    JOIN player ON player1_id = player.id
    WHERE eventmsgtype = 4
    GROUP BY game_id, player1_id
""")
data_to_import = sourceCursor.fetchall()

init = 0
for data in data_to_import:
    game_id, player_id, rebound = data
    cursor.execute("""
        INSERT OR IGNORE INTO gamerecord (GID, PID, Rebound, Score)
        VALUES (?, ?, ?, ?)
    """, (game_id, player_id, rebound, init))
    cursor.execute("""
        UPDATE gamerecord
        SET Rebound = ?
        WHERE GID = ?
        AND PID = ?
    """, (rebound, game_id, player_id))

conn.commit()
conn.close()
source.close()

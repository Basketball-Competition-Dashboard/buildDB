import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# 計算抄截數
sourceCursor.execute("""
    SELECT game_id, player2_id, count(*)
    FROM play_by_play
    JOIN player ON player2_id = player.id
    WHERE eventmsgtype = 5
    GROUP BY game_id, player2_id
""")
data_to_import = sourceCursor.fetchall()

for data in data_to_import:
    game_id, player_id, steal = data
    cursor.execute("""
        INSERT OR IGNORE INTO gamerecord (GID, PID, Steal)
        VALUES (?, ?, ?)
    """, (game_id, player_id, steal))
    cursor.execute("""
        UPDATE gamerecord
        SET Steal = ?
        WHERE GID = ?
        AND PID = ?
    """, (steal, game_id, player_id))

conn.commit()
conn.close()
source.close()

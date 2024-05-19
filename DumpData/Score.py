import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# 計算 3 分球得分
sourceCursor.execute("""
    SELECT game_id, player1_id, count(*) * 3
    FROM play_by_play
    WHERE eventmsgtype = 1
    AND eventmsgactiontype = 1
    GROUP BY game_id, player1_id
""")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, score = data
    cursor.execute("""
        INSERT OR IGNORE INTO gamerecord (GID, PID, Score)
        VALUES (?, ?, ?)
    """, (game_id, player_id, score))
    cursor.execute("""
        UPDATE gamerecord
        SET score = score + ?
        WHERE GID = ?
        AND PID = ?
    """, (score, game_id, player_id))

# 計算 2 分球得分
sourceCursor.execute("""
    SELECT game_id, player1_id, count(*) * 2
    FROM play_by_play
    WHERE eventmsgtype = 1
    AND eventmsgactiontype != 1
    GROUP BY game_id, player1_id
""")
data_to_import = sourceCursor.fetchall()
for data in data_to_import:
    game_id, player_id, score = data
    cursor.execute("""
        INSERT OR IGNORE INTO gamerecord (GID, PID, Score)
        VALUES (?, ?, ?)
    """, (game_id, player_id, score))
    cursor.execute("""
        UPDATE gamerecord
        SET score = score + ?
        WHERE GID = ?
        AND PID = ?
    """, (score, game_id, player_id))

conn.commit()
conn.close()
source.close()

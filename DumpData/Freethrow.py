import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# ***請先執行Score.py得到分數後再執行罰球得到的分數
# ***罰球數並不會算入Hit

# 計算罰球數
sourceCursor.execute("""
SELECT
    game_id,
    player1_id ,
    COUNT(CASE WHEN eventmsgtype = 3 AND score is not null THEN 1 ELSE NULL END) AS freethrows
FROM
    play_by_play
WHERE
    eventmsgtype = 3
GROUP BY
    game_id,
    player1_id;
""")
data_to_import = sourceCursor.fetchall()

for data in data_to_import:
    game_id, player_id, free_throws = data
    cursor.execute("""
        INSERT OR IGNORE INTO gamerecord (GID, PID, FreeThrow)
        VALUES (?, ?, ?)
    """, (game_id, player_id, free_throws))
    cursor.execute("""
        UPDATE gamerecord
        SET FreeThrow = ?
        WHERE GID = ?
        AND PID = ?
    """, (free_throws, game_id, player_id))
    cursor.execute("""
        UPDATE gamerecord
        SET Score = Score + ?
        WHERE GID = ?
        AND PID = ?
    """, (free_throws, game_id, player_id))


conn.commit()
conn.close()
source.close()

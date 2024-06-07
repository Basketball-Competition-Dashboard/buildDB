import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

sourceCursor.execute("""
SELECT 
    game.game_id, game.team_id_home, game.team_id_away, game.pts_home, game.pts_away, game.wl_home, game.wl_away
FROM 
    game
WHERE 
    team_id_away in (SELECT id from team) AND
    team_id_home in (SELECT id from team)
""")
data_to_import = sourceCursor.fetchall()

to_db = []
for gid, team_id_home, team_id_away, score_home, score_away, wl_home, wl_away in data_to_import:
    # 将主场队伍插入到 Attend 表中
    to_db.append((gid, team_id_home, True, score_home, wl_home))
    # 将客场队伍插入到 Attend 表中
    to_db.append((gid, team_id_away, False, score_away, wl_away))

cursor.executemany("""
    INSERT OR IGNORE INTO Attend (GID, TID, is_home_team, Score, is_win_team) 
    VALUES (?,?,?,?,?);
""", to_db)

conn.commit()
conn.close()
source.close()

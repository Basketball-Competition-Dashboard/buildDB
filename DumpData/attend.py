import sqlite3

# 连接到数据库
conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

# 从 source 数据库中选择数据
sourceCursor.execute("""
    SELECT line_score.game_id, line_score.team_id_home, line_score.team_id_away, 
           line_score.pts_home, line_score.pts_away, game.wl_home, game.wl_away
    FROM line_score 
    JOIN team ON (line_score.team_id_home = team.id OR line_score.team_id_away = team.id) 
    JOIN game ON line_score.game_id = game.game_id;
""")
data_to_import = sourceCursor.fetchall()

# 准备插入 Attend 表的数据
to_db = []
for gid, team_id_home, team_id_away, score_home, score_away, wl_home, wl_away in data_to_import:
    # 将主场队伍插入到 Attend 表中
    to_db.append((gid, team_id_home, True, score_home, wl_home))
    # 将客场队伍插入到 Attend 表中
    to_db.append((gid, team_id_away, False, score_away, wl_away))

# 插入数据到 SQLite 数据表
cursor.executemany("""
    INSERT OR IGNORE INTO Attend (GID, TID, is_home_team, Score) 
    VALUES (?,?,?,?);
""", to_db)

# 提交更改并关闭连接
conn.commit()
conn.close()
source.close()

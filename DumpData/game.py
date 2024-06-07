import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

sourceCursor.execute("""
SELECT 
    game_id, game_date, season_id, team.city 
FROM 
    game
JOIN 
    team ON team.id = team_id_home
""")
data_to_import = sourceCursor.fetchall()

for data in data_to_import:
    game_id, game_date, season_id, city  = data
    cursor.execute("""
        INSERT OR IGNORE INTO Game (GID, Date, Place, SID) 
        VALUES (?,?,?,?);
    """, (game_id, game_date, city, season_id))

conn.commit()
conn.close()
source.close()

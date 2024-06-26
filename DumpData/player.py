import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

sourceCursor.execute("""
SELECT 
    person_id, first_name, last_name, birthdate, height, weight, position, country, team_id
FROM 
    common_player_info
JOIN 
    team ON common_player_info.team_id = team.id
""")
data_to_import = sourceCursor.fetchall()

cursor.executemany("""
    INSERT INTO Player (PID, FName, LName, Bdate, Height, Weight, Position, Country, TID) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?);
""", data_to_import)

conn.commit()
conn.close()
source.close()
import sqlite3

conn = sqlite3.connect('nbaDB.db')
cursor = conn.cursor()
source = sqlite3.connect("nba.sqlite")
sourceCursor = source.cursor()

sourceCursor.execute("""
SELECT 
    id, full_name, team.city, headcoach, year_founded, team.abbreviation, team.nickname 
FROM 
    team
LEFT JOIN 
    team_details ON team.id = team_details.team_id
""")
data_to_import = sourceCursor.fetchall()

cursor.executemany("""
    INSERT OR IGNORE INTO Team (TID, TName, City, CoachName, YearFounded, NameAbbr, NickName) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", data_to_import)

conn.commit()
conn.close()
source.close()

CREATE TABLE "Attend" (
	"GID"	INTEGER NOT NULL,
	"TID"	INTEGER NOT NULL,
	"is_home_team"	bool,
	"Score"	INTEGER,
	"is_win_team"	TEXT,
	PRIMARY KEY("GID","TID"),
	FOREIGN KEY("GID") REFERENCES "Game"("GID") ON DELETE CASCADE,
	FOREIGN KEY("TID") REFERENCES "Team"("TID") ON DELETE CASCADE
);
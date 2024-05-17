CREATE TABLE "GameRecord" (
	"PID"	TEXT NOT NULL,
	"GID"	TEXT NOT NULL,
	"Assist"	INTEGER,
	"Hit"	INTEGER,
	"Steal"	INTEGER,
	"Rebound"	INTEGER,
	"Score"	INTEGER,
	"FreeThrow"	INTEGER,
	PRIMARY KEY("PID","GID"),
	FOREIGN KEY("PID") REFERENCES "Player"("PID"),
	FOREIGN KEY("GID") REFERENCES "Game"("GID")
);
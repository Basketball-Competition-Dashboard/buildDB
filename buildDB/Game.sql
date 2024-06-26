CREATE TABLE "Game" (
	"GID"	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	"Date"	Date,
	"Place"	TEXT,
	"SID"	INTEGER NOT NULL,
	FOREIGN KEY("SID") REFERENCES "Season"("SID") ON DELETE CASCADE
);
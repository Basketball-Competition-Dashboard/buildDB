CREATE TABLE "Game" (
	"GID"	INTEGER NOT NULL,
	"Date"	Date,
	"Place"	TEXT,
	"SID"	INTEGER NOT NULL,
	FOREIGN KEY("SID") REFERENCES "Season"("SID") ON UPDATE CASCADE,
	PRIMARY KEY("GID")
);
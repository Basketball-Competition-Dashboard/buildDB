CREATE TABLE "Player" (
	"PID"	INTEGER NOT NULL,
	"FName"	TEXT,
	"LName"	TEXT,
	"Bdate"	DATE,
	"Height"	float,
	"Weight"	float,
	"Position"	TEXT,
	"Country"	TEXT,
	"TID"	INTEGER NOT NULL,
	PRIMARY KEY("PID"),
	FOREIGN KEY("TID") REFERENCES "Team"("TID") ON DELETE CASCADE
);
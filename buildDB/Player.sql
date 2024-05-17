CREATE TABLE "Player" (
	"PID"	TEXT NOT NULL,
	"FName"	TEXT,
	"LName"	TEXT,
	"Bdate"	DATE,
	"Height"	float,
	"Weight"	float,
	"Position"	TEXT,
	"Country"	TEXT,
	"TID"	TEXT,
	PRIMARY KEY("PID"),
	FOREIGN KEY("TID") REFERENCES "Team"("TID") ON UPDATE CASCADE
);
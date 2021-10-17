CREATE TABLE "compras" (
	"id"	INTEGER,
	"fecha"	TEXT NOT NULL,
	"hora"	TEXT NOT NULL,
	"coinFrom"	TEXT,
	"cantFrom"	REAL,
	"coinTo"	TEXT,
	"cantTo"	REAL,
	"Pu"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
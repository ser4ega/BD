import sqlite3 

conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 


c.execute(""" 
CREATE TABLE IF NOT EXISTS Acii ( 
id INTEGER PRIMARY KEY, 
Name TEXT, 
Type Text,
CHECK( 
Type = "обычные" OR 
Type = "привелигированные" OR 
Type = "фьючерс" 
)

); 
""") 


c.execute(""" 
CREATE TABLE IF NOT EXISTS Kurs ( 
id INTEGER PRIMARY KEY, 
Name TEXT, 
Date DATETIME,
Cena INTEGER,
Acii_id INTEGER,
FOREIGN KEY (Acii_id) REFERENCES 
Acii(id) ON DELETE CASCADE 
); 
""") 

c.execute(""" 
CREATE TABLE IF NOT EXISTS Operacii ( 
id INTEGER PRIMARY KEY, 
Date DATETIME,
Name TEXT,
Kolichestvo INTEGER,
Type TEXT,
Acii_id INTEGER,
CHECK( 
Type = "покупка" OR 
Type = "продажа" OR 
Type = "опцион" 
),

FOREIGN KEY (Acii_id) REFERENCES Acii(id) ON DELETE RESTRICT
);

""") 


# SELECT sql FROM sqlite_master
# WHERE tbl_name = 'GROUPS' AND type = 'table'

conn.commit() 
conn.close()
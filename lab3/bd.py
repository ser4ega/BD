import sqlite3 

conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 


c.execute(""" 
CREATE TABLE IF NOT EXISTS GROUPS ( 
id INTEGER PRIMARY KEY, 
Floor INTEGER, 
Class INTEGER UNIQUE
); 
""") 


c.execute(""" 
CREATE TABLE IF NOT EXISTS CHILDREN ( 
id INTEGER PRIMARY KEY, 
Name TEXT, 
Age INTEGER,
Group_id INTEGER,
CHECK( 
Age > 0 AND
Age < 7
), 
FOREIGN KEY (Group_id) REFERENCES 
GROUPS(id) ON DELETE RESTRICT 
); 
""") 

c.execute(""" 
CREATE TABLE IF NOT EXISTS ATTENDANCE ( 
Child_id INTEGER, 
Group_id INTEGER, 
Date DATETIME,
FOREIGN KEY (Child_id) REFERENCES CHILDREN(id) ON DELETE CASCADE,
FOREIGN KEY (Group_id) REFERENCES GROUPS(id) ON DELETE RESTRICT 

);

""") 


# SELECT sql FROM sqlite_master
# WHERE tbl_name = 'GROUPS' AND type = 'table'

conn.commit() 
conn.close()
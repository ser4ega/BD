import sqlite3 

conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 

# создаем таблицу Acii
# CHECK проверяет, что значение Type , будет одним из ['обычные', 'привелигированные', 'фьючерс']
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

# создаем таблицу Kurs
# FOREIGN KEY (Acii_id) REFERENCES  - связь с таблицей Acii через Acii_id - id акции
# Acii(id) ON DELETE CASCADE - при попытке удалить запись из таблицы Acii, каскадно удалить все ссылающиеся на id этой записи таблицы Kurs
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
# создааем таблицу Operacii
# CHECK() проверяет, что значение ключа Type будет одним из ['покупка', 'продажа', 'опцион']
# FOREIGN KEY (Acii_id) REFERENCES Acii(id)  - связь с таблицей Acii через Acii_id - id акции
# ON DELETE RESTRICT  - при попытке удалить запись из таблицы Acii, запретить удаление, если на нее ссылается хотя бы одна запись из таблицы Operacii
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



conn.commit() 
conn.close()
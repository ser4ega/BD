import sqlite3 
import random 
import datetime 
import string
conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 
Acii_Types=[
    "обычные","привелигированные","фьючерс"
]
Operacii_Types=[
    "покупка","продажа","опцион"
]
    # zapolnyaem Aciii
def randomName(stringLength=random.randint(5,10)):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


for i in range(20):   
    
    c.execute('INSERT INTO Acii ( Name, Type) VALUES (?, ?)', 
    ( 
    randomName(),
    random.choice(Acii_Types)
    ) 
    ) 
    # fill children
    
def randomDate(
    start_date = datetime.datetime(2010, 1,1,0,0,0), 
    end_date = datetime.datetime(2019, 12, 31,23,59,59) 
    ):
    return start_date+(start_date - end_date)*random.random()
for i in range(30):     
    query="""INSERT INTO Kurs(        
        Name , 
        Date ,
        Cena ,
        Acii_id 
    ) VALUES 
    (?,?,?,?)""" 
    c.execute(query,(
        randomName(),
        randomDate(),
        random.uniform(0.000001, 100000),
        c.execute("SELECT * FROM Acii ORDER BY RANDOM() LIMIT 1").fetchall()[0][0]
        
    ) )


for i in range(1000):         
    c.execute('''INSERT INTO Operacii ( 
        Date ,
        Name ,
        Kolichestvo ,
        Type ,
        Acii_id
        ) VALUES (?, ?, ?, ?, ?)''', 
    ( 
        randomDate(),
        randomName(),
        random.randint(1,10000),
        random.choice(Operacii_Types),
        c.execute("SELECT * FROM Acii ORDER BY RANDOM() LIMIT 1").fetchall()[0][0]
    ) 
    ) 
print('End')
# c.execute('DELETE FROM CHILDREN')

conn.commit() 
conn.close()
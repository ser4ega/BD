import sqlite3 
import random 
import datetime 
conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 
# если захочется поинкрементировать: 
def max_id(table):
    global c
    c.execute(f"SELECT COUNT(*) FROM {table};")
    numrows=c.fetchall()[0][0]
    if numrows>0:
        res=c.execute(f"""SELECT * FROM {table} 
            ORDER BY id DESC LIMIT 1""").fetchall()
        id0=res[0][0] + 1
    else:
        id0=0
    return id0
# чтобы классы были уникальными составляем мно-во 
#       использованных значений
classes=set()
query="SELECT * FROM GROUPS"
result=c.execute(query).fetchall()
if(len(result)>0):
    for i in range(len(result)):
        classes.add(result[i][2])
# полное множество классов
# и вычитаем одно из другого, получая множество доступных классов
# и выбираем один из доступных
def random_class(max):
    global classes
    all_classes={i+1 for i in range(max)}
    available_classes=all_classes-classes
    if (available_classes):
        res=random.choice(list(available_classes))
    else:
        print('ERROR: No available classes')
        return None
    
    classes.add(res)
    return res

    # fill groups
for i in range(20): 
     
    cur_class=random_class(100)# если классов всего 50, не пытайтесь сделать больше 50 записей
    if cur_class==None:
        cur_floor=None
    else:
        cur_floor=cur_class//10+1 # (10 классов на этаже)
    c.execute('INSERT INTO GROUPS ( Floor, Class) VALUES (?, ?)', 
    ( 
    cur_floor,
    cur_class
    ) 
    ) 
    # fill children
names=['Олег', 'Николай', 'Евгений', 'Максим', 'Оля', 'Катя', 'Юля', 'Настя']
surnames=['Сидоренко', 'Петренко', 'Красненко', 'Иванько', 'Садко', 'Губко']


for i in range(30):     
    query="""INSERT INTO CHILDREN( 
    Name , 
    Age , 
    Group_id
    ) VALUES 
    (?,?,?)""" 
    c.execute(query,(
        random.choice(surnames)+" "+random.choice(names),
        random.randint(1,6),
        c.execute("SELECT * FROM GROUPS ORDER BY RANDOM() LIMIT 1").fetchall()[0][0]
        
    ) )

start_date = datetime.datetime(2016, 1,1,0,0,0) 
end_date = datetime.datetime(2019, 12, 31,23,59,59) 
for i in range(1000):  
    child=c.execute("SELECT * FROM CHILDREN ORDER BY RANDOM() LIMIT 1").fetchall()   
    c.execute('''INSERT INTO ATTENDANCE ( 
        Child_id, 
        Group_id, 
        Date
        ) VALUES (?, ?, ?)''', 
    ( 
        
        child[0][0], # Child_id
        child[0][3], # Group_id
        start_date+(start_date - end_date)*random.random(),
    ) 
    ) 
print('End')
# c.execute('DELETE FROM CHILDREN')

conn.commit() 
conn.close()
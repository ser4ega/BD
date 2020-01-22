import sqlite3 
import random 
import datetime 
import string
# подключаемся к базе данных
conn = sqlite3.connect('Lab3.db') 
# создаем курсор на бд
c = conn.cursor() 
# включаем проверку заграничных ключей (внешних)
conn.execute('PRAGMA foreign_keys = ON') 
# массив возможных значений для типов акций
Acii_Types=[
    "обычные","привелигированные","фьючерс"
]
# массив возможных значений для типов операций
Operacii_Types=[
    "покупка","продажа","опцион"
]
    
# самописная функция для генерации случайной строки длиной от 5 до 10 символов
def randomName(stringLength=random.randint(5,10)):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase # буквы
    return ''.join(random.choice(letters) for i in range(stringLength)) # создание строки из букв

# заполняем таблицу акции в цикле (+20 записей)
for i in range(20):   
    
    c.execute('INSERT INTO Acii ( Name, Type) VALUES (?, ?)', 
    ( 
    randomName(),
    random.choice(Acii_Types) # случайный выбор из массива Acii_Types
    ) 
    ) 
    # fill children
# самописная функция генерации даты
def randomDate(
    start_date = datetime.datetime(2010, 1,1,0,0,0), 
    end_date = datetime.datetime(2019, 12, 31,23,59,59) 
    ):
    return start_date+(start_date - end_date)*random.random() # random.random() - возвращает дробное число в диапазоне от 0 до 1

# заполняем таблицу Kurs (+30)
for i in range(30):     
    query="""INSERT INTO Kurs(        
        Name , 
        Date ,
        Cena ,
        Acii_id 
    ) VALUES 
    (?,?,?,?)""" 
    c.execute(query,(
        randomName(), # случайное имя
        randomDate(), # случайная дата
        random.uniform(0.000001, 100000), # случайной дробное в диапазоне от 0.000001 до 100000
        c.execute("SELECT * FROM Acii ORDER BY RANDOM() LIMIT 1").fetchall()[0][0] # чтобы соблюдалась связь с таблицей Acii, рандомный Acii_id берем из нее
        # при помощи запроса "SELECT * FROM Acii ORDER BY RANDOM() LIMIT 1" 
        # т.к. запрос возвращает массив массивов (массив из записей, а каждая запись - массив ключей) 
        # , а мы хотим получить только первый ключ первой записи, при распаковке ответа fetchall() забираем элемент с индексом [0][0]
        
    ) )

# заполняем таблицу Operacii (+1000)
for i in range(1000):         
    c.execute('''INSERT INTO Operacii ( 
        Date ,
        Name ,
        Kolichestvo ,
        Type ,
        Acii_id
        ) VALUES (?, ?, ?, ?, ?)''', 
    ( 
        randomDate(), # случайная дата
        randomName(), # случайное имя
        random.randint(1,10000), # случайное целое число в диапазоне от 1 до 100000
        random.choice(Operacii_Types), # случайный элемент из массива Operacii_types
        c.execute("SELECT * FROM Acii ORDER BY RANDOM() LIMIT 1").fetchall()[0][0] # аналогично как в предыдущем, для соблюдения связи таблиц
        # заполняем Acii_id случайным значением id из таблицы Acii
    ) 
    ) 
print('End')
# c.execute('DELETE FROM CHILDREN')

conn.commit() 
conn.close()
from sys import *
from peewee import *
import random


cinema_id=0
Films = ['Ono','Snow white','Thing','Godzilla','Joker','Batman', 'Archi']
Genres=['horror','documentalistic','comedy','fight art']
Descriptions=['good film, actors reaally cool','i like that film soooo much','this film is good, but Joker are better']

db = SqliteDatabase('cinema.db')

def add_random_cinema():    
    global cinema_id  
    cinema_id+=1
    row = Cinema.create(
        id=cinema_id,
        Film=random.choice(Films),
        Description=random.choice(Descriptions),
        Genre=random.choice(Genres)
    )
    row.save()

class BaseModel(Model):
    class Meta:
        database = db

class Cinema(BaseModel):
    id=PrimaryKeyField()
    Film = CharField()
    Description = CharField()
    Genre = CharField()
    class Meta:
        db_table="Cinema"   

db.create_tables([Cinema])
db.drop_tables([Cinema])
db.create_tables([Cinema])
'''
if __name__ == 'main':

    try:
        db.connect()
        Cinema.create_table()
    except InternalError as px:
        print('Hello')
        print(str(px))
'''


for i in range(10):
    add_random_cinema()
res=Cinema.select()
print("%-20s%-20s%-50s%-20s"%("id:","Film:","Description:","Genre:"))
for i in res:
    print("%-20s%-20s%-50s%-20s"%(i.id,i.Film,i.Description,i.Genre))     






def add_cinema(): 
    global cinema_id   
    cinema_id+=1    
    Genre=input('Введите название жанра: ')    
    Film= input('ВВедите название фильма: ')
    Description=input('ВВедите описание фильма: ')
    row = Cinema.create(
        id=cinema_id,
        Film=Film,
        Description=Description,
        Genre=Genre
    )
    row.save()

def show_res(res):
    print('')
    print("%-20s%-20s%-50s%-20s"%("id:","Film:","Description:","Genre:"))
    for i in res:
        print("%-20s%-20s%-50s%-20s"%(i.id,i.Film,i.Description,i.Genre))

def add_new():
    n=int(input("Сколько записей хотите добавить? "))
    for i in range(n):
        print("ВВедите ",i+1,' запись\n')
        add_cinema()
    res=Cinema.select()
    show_res(res)
        
def main_menu():
    switch=int(input('''Что вы хотите?
    1.Добавить записи
    2.Найти записи
    3.Удалить записи
    4.Ничего
    '''))

    while(switch<1 or switch >4):

        switch=int(input('''Что вы хотите?
    1.Добавить записи
    2.Найти записи
    3.Удалить записи
    4.Ничего
    '''))

    if(switch==1):
        add_new()
    elif(switch==2):
        find_existed()    
    elif(switch==3):
        delete_existed()
    elif(switch==4):
        return
    main_menu()

def find_existed():
    switch=int(input('''Выбрать фильмы по: 
    0.Вывести все записи
    1.Жанру
    2.Названию
    3.ID
    '''))

    while(switch<0 or switch >3):

        switch=int(input('''Выбрать фильмы по: 
    0.Вывести все записи
    1.Жанру
    2.Названию
    3.ID
    '''))
    if(switch==0):
        res=Cinema.select()
    if(switch==1):
        genre=input("Введите жанр: ")
        res=Cinema.select().where(Cinema.Genre==genre)
        
    elif(switch==2):
        Film=input("Введите название: ")
        res=Cinema.select().where(Cinema.Film==Film)
       
    elif(switch==3):
        id=input("Введите ID: ")
        res=Cinema.select().where(Cinema.id==id)    
    show_res(res)





def delete_existed():
    switch=int(input('''Выбрать записи на удаление по: 
    0.Удалить все
    1.Жанру
    2.Названию
    3.ID
    '''))

    while(switch<0 or switch >3):

        switch=int(input('''Выбрать записи на удаление по: 
    0.Удалить все
    1.Жанру
    2.Названию
    3.ID
    '''))
    if(switch==0):        
        q = Cinema.delete()
    if(switch==1):
        Genre=input("Введите жанр: ")
        q = Cinema.delete().where(Cinema.Genre == Genre)
    elif(switch==2):
        Film=input("Введите название: ")
        q=Cinema.delete().where(Cinema.Film==Film)
    elif(switch==3):
        id=int(input("Введите ID: "))
        q=Cinema.delete().where(Cinema.id==id)
    q.execute()
    res=Cinema.select()
    show_res(res)

main_menu()



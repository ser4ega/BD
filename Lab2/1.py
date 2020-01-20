import sqlite3
import random
import datetime
conn=sqlite3.connect('Sales.db')

k=conn.cursor()

k.execute('''CREATE TABLE IF NOT EXISTS Sales (    
    Id INTEGER PRIMARY KEY,
    Country TEXT, 
    City TEXT, 
    Shop TEXT, 
    Date DATETIME, 
    Money INTEGER
    );
    ''')


Countries = [ 'Russia',
           'German',
           'Ukrain',
           'UK']
Cities = {'Russia':
        ['Moscow', 'Belgorod', 'St. Petersburg', 'Kogalym'],
        'German':
        ['Berlin', 'Munich ', 'Frankfurt', 'Dortmund '],
        'Ukrain':
        ['Kiev', 'Odessa', 'Minsk', 'Varsaw' ],
        'UK':
        ['London', 'Manchester', 'Liverpool', 'Glasgow']}
Shops = ['Taobao', 'Amazon','Aliexpress','eBay']

f = open("result.txt", "w",encoding='utf-8')


start_date=datetime.datetime(2014, 1, 1,0,0,0)
end_date = datetime.datetime(2015, 1, 1,0,0,0)

for i in range(10000):
    cur_country=random.choice(Countries)
    cur_city=random.choice(Cities[cur_country])
    cur_shop=random.choice(Shops)
    cur_date=start_date+(end_date-start_date)*random.random()
    cur_int=random.randint(10000,1000000)
    k.execute( '''INSERT INTO Sales(
        Country , 
        City , 
        Shop , 
        Date , 
        Money ) VALUES ( ?, ?, ?, ?, ?)''',
        (
            
            cur_country,
            cur_city,
            cur_shop,
            cur_date,
            cur_int
        )   
    )
    if(i<100):
        f.writelines(str(i)+"\t")
        f.writelines(cur_country+"\t")
        f.writelines(cur_city+"\t")
        f.writelines(cur_shop+"\t")
        f.writelines(str(cur_date)+"\t")
        f.writelines(str(cur_int)+"\t\n")



f.writelines('Задание 1\n')
query = 'SELECT COUNT(*) FROM Sales'
k.execute(query)
f.writelines([query,"\nКоличество записей:" + str(k.fetchall()[0][0])+"\n"])


f.writelines('Задание 2\n')

query = 'Select Country, count(Shop) from Sales group by Country'
f.writelines([query,"\nКоличество магазинов в стране:\n"])
res=k.execute(query).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')




f.writelines('Задание 3\n')
query = 'SELECT Shop, SUM(Money) FROM Sales GROUP BY Shop'
f.writelines([query,"\nСумма продаж по магазинам:\n"])
k.execute(query)
res=k.fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')
    


f.writelines('Задание 4\n')
query='''SELECT Shop, SUM(Money) FROM Sales WHERE (Country = ? AND 
Date BETWEEN "2014-06-01" AND "2014-09-01") GROUP BY Shop'''
cur_country = input("\nВведите страну: ")
f.writelines([query,"\nВ стране "+cur_country+" выручка за лето составила\n"])

res=k.execute(query, (cur_country, )).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')

f.close()
conn.commit()
conn.close()
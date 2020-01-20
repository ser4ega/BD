import sqlite3
conn = sqlite3.connect('Sales.db')
k = conn.cursor()

f = open("result2.txt", "w",encoding='utf-8')

query = "SELECT DISTINCT *  FROM Shops"
f.writelines('Задание 1\n')
f.writelines('''выбрать уникальные записи shop_id, 
city, country - запросом (уникальные, это значит не повторяющиеся)\n''')
k.execute(query)
f.writelines([query,'\n'])


f.writelines('Задание 4\n')
f.writelines(' Показать сумму продаж в определенной стране по магазинам за лето.\n')
query='''SELECT Country, Shop, SUM(Money) 
FROM (SELECT * FROM Shops INNER JOIN (SELECT * FROM Sales) on Shop_id=id) 
WHERE (Country=? AND Date BETWEEN "2014-06-01" AND "2014-08-31")
GROUP BY Shop'''
cur_country = input("\nВведите страну: ")
f.writelines([query,"\nВ стране "+cur_country+" выручка за лето составила\n"])

res=k.execute(query, (cur_country, )).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')

query = '''SELECT Country,City, SUM(Money)
FROM (SELECT Country,City, Money from Shops INNER JOIN (SELECT * from Sales) on Shop_id=id)
GROUP BY City
ORDER BY Country
'''
f.write('\nЗадание 5\n')
f.write("Средняя сумма продаж по городам:\n")
f.write(query + "\n\n")
res=k.execute(query).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')




query = 'SELECT Shop,AVG(Money) FROM Sales group by shop'
f.write('\nЗадание 6\n')
f.write("Средняя сумма продаж по магазинам:\n")
f.write(query + "\n\n")
res=k.execute(query).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')

query = '''SELECT Country,AVG(Money) 
FROM (SELECT Country, Money from Shops INNER JOIN Sales on Shop_id=id) 
group by Country'''
f.write('\nЗадание 6\n')
f.write("Средняя сумма продаж по городам:\n")
f.write(query + "\n\n")
res=k.execute(query).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')

query = '''SELECT Country,AVG(Money) 
FROM (SELECT Country,Money from Shops INNER JOIN Sales on Shop_id=id) 
group by Country'''
f.write('\nЗадание 6\n')
f.write("Средняя сумма продаж по странам:\n")
f.write(query + "\n\n")
res=k.execute(query).fetchall()
for i in res:
    f.writelines(str(j)+'\t' for j in i)
    f.write('\n')


f.close()

conn.commit()
conn.close()
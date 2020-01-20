import sqlite3
conn = sqlite3.connect('Sales.db')
k = conn.cursor()
k.execute('''
    CREATE TABLE IF NOT EXISTS Shops (
        Shop_id INTEGER,
        Country TEXT,
        City TEXT
        );
    ''')

k.execute('''
    INSERT INTO Shops
        SELECT Id, Country, City FROM Sales
        GROUP BY Id
    ''')
k.execute(
'''BEGIN TRANSACTION;
CREATE TABLE SalesNew AS SELECT Id, Shop, Date, Money FROM Sales; 
DROP TABLE Sales; 
ALTER TABLE SalesNew RENAME TO Sales; 
COMMIT;''')

conn.commit()
conn.close()
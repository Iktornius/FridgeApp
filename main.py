import sqlite3

inp=input('Zawartosc lodowki to: ')

lodowka=inp.split(',')

con = sqlite3.connect('baza.db')

c = con.cursor()

c.execute('SELECT Składniki FROM posts')

all_rows = c.fetchall()

for n in all_rows[0]:
    print(i[0])



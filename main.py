import sqlite3
from operator import itemgetter

inp=input('Zawartosc lodowki to: ').lower()

lodowka=inp.split(',')

con = sqlite3.connect('baza.db')

c = con.cursor()

c.execute('SELECT * FROM posts')

all_rows = c.fetchall()

lista=[]
listaproc=[]


for i in all_rows:
    k=i[1].lower()
    l=set(inp).intersection(k)
    lista.append(i[0])
    listaproc.append(int((len(l)/len(k))*100))

slownik=dict(zip(lista, listaproc))
koniec=sorted(slownik.items(), key=itemgetter(1), reverse=True)

print ("Propozycje dań:")
for elem in koniec[0:5]:
    print ("{0} - {1}%".format(elem[0], elem[1]))


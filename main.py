import sqlite3, webbrowser
from operator import itemgetter

inp=input('Zawartosc lodowki to: \n').lower()

lodowka=set(inp.split(', '))

con = sqlite3.connect('baza.db')

c = con.cursor()

c.execute('SELECT * FROM posts')

all_rows = c.fetchall()

lista=[]
listaproc=[]

for i in all_rows:
    k=i[1].lower()
    m=k.split(', ')
    l=set(lodowka).intersection(m)
    if len(l)!=0:
        lista.append(i[0])
        listaproc.append(int((len(l)/len(m))*100))


slownik=dict(zip(lista, listaproc))
koniec=sorted(slownik.items(), key=itemgetter(1), reverse=True)

count = 1

if len(koniec)!=0:
    print("Propozycje dań:")
    for elem in koniec[0:5]:
        if elem[1]!=0:
            print("{0}. {1} - {2}%".format(count, elem[0], elem[1]))
        count+=1
    print('\n')
else:
    print("Ups, nie znalazłem pasujących dań! \n")

wybor=input('Wyszukać najlepszy wynik w Google? (Tak/Nie)  \n')
if wybor.lower()=='tak':
    przepis=koniec[0][0].split(' ')
    url='+'.join(przepis)
    webbrowser.open('http://www.google.com/search?q={0}+przepis'.format(url))
    print('Otwieram przeglądarke, smacznego! ...')

else:
    print("Smacznego!")






import sqlite3

with sqlite3.connect("baza.db") as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE posts""")
    c.execute("CREATE TABLE posts(Przepis TEXT, Składniki TEXT)")
    c.execute('INSERT INTO posts VALUES("Gołąbki", "Kapusta, ryż, mięso")')
    c.execute('INSERT INTO posts VALUES("Pierogi", "Ziemniaki, ser biały, cebula, mąka, woda")')
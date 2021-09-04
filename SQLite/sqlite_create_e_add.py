import sqlite3

banco = sqlite3.connect('data_base.db')

cursor = banco.cursor()

""" cursor.execute("CREATE TABLE livros (titulo text, autor text, id integer)") """

""" cursor.execute("INSERT INTO livros VALUES('Quincas Borba', 'Machado de Assis', 1)") """
""" banco.commit() """

cursor.execute("SELECT * FROM livros")
print(cursor.fetchall())
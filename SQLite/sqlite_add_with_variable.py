import sqlite3

banco = sqlite3.connect('data_base.db')

machado2 = 'Memórias Póstumas', 'Machado de Assis', 2

cursor = banco.cursor()

""" cursor.execute("INSERT INTO livros VALUES('"+machado2[0]+"', '"+machado2[1]+"', '"+str(machado2[2])+"')") 
banco.commit() 
 """
cursor.execute('SELECT * FROM livros')
print(cursor.fetchall())
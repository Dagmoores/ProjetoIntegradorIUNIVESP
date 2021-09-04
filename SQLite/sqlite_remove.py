import sqlite3


try:
    banco = sqlite3.connect('data_base.db')

    cursor = banco.cursor()

    cursor.execute("DELETE FROM livros WHERE id = 1")
    banco.commit()
    banco.close()
    print("Excluído com sucesso")

except sqlite3.Error as erro:
    print("Erro ao excluir")
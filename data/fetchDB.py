import sqlite3

conn = sqlite3.connect('people.db')

cursor = conn.execute("SELECT * from People where MINISTERIO = 'Alabanza'")

test = cursor.fetchall()

for row in test:
  pyscript.write('MIN',row[1])
  pyscript.write('NOMBRE', row[2])
  pyscript.write('EDAD', row[3])
  pyscript.write('DOC_ID', row[4])
  pyscript.write('PHONE', row[5])
  pyscript.write('T_CR', row[6])
  pyscript.write('CURSOS', row[7])

conn.close()

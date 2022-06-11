import sqlite3

conn = sqlite3.connect('people.db')

cursor = conn.execute("insert into people(MINISTERIO,NOMBRE,EDAD,DOC_ID,PHONE,T_CR,CURSOS) values (?,?,?,?,?,?,?)", ("Alabanza", "Ildebrancio Cantor",25,456123,3576842,"5 años","ADN,LLP"))

conn.close()
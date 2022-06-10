import sqlite3

conexion=sqlite3.connect('./data/people.db')
conexion.execute("insert into people(MINISTERIO,NOMBRE,EDAD,DOC_ID,PHONE,T_CR,CURSOS) values (?,?,?,?,?,?,?)", ("Alabanza", "Ildebrancio Cantor",25,456123,3576842,"5 años","ADN,LLP"))                    
conexion.close()
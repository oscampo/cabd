import sqlite3

conn = sqlite3.connect('./data/people.db')

conn.execute('''INSERT INTO People (ID,MINISTERIO,NOMBRE,EDAD,DOC_ID,PHONE,T_CR,CURSOS) VALUES (3,"Alabanza", "Ildebrancio Cantor",25,456123,3576842,"5 años","ADN,LLP")''');
conn.commit()
conn.close()
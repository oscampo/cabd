import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'people.db')
conexion=sqlite3.connect(db_path)
conexion.execute("insert into people(MINISTERIO,NOMBRE,EDAD,DOC_ID,PHONE,T_CR,CURSOS) values (?,?,?,?,?,?,?)", ("Alabanza", "Ildebrancio Cantor",25,456123,3576842,"5 años","ADN,LLP"))                    
conexion.close()
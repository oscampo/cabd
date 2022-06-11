import sqlite3

conn = sqlite3.connect('people.db')

cursor = conn.execute("insert into People values (?,?,?,?,?,?,?,?)", (3,"Alabanza", "Ildebrancio Cantor",25,456123,3576842,"5 años","ADN,LLP"))

conn.close()
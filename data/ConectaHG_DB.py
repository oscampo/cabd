import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='162.241.61.240',
                                     database='iblicrca_aspirantes',
                                         user='iblicrca_directores',
                                         password='Nu3Vos5i3rVos')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
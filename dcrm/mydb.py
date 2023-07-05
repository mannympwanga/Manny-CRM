import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='manny@nf201',
    auth_plugin='mysql_native_password'
)


cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE mannydrcm")

print("All Done!")
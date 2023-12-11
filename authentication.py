import connection_db

def authentication_function(usr,psw):
    sql = 'SELECT * FROM users WHERE username = %s AND password = %s'
    valori = (usr.get(), psw.get())
    connection_db.cursor.execute(sql, valori)
    result = connection_db.cursor.fetchall()
    if result:
        return True
    
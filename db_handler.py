import connect as c
'''
This is a functions page that will handle all of the data that gets sent
to and from the API. Each function is used in unison with the connection class
in order to send, retrieve, update, or delete data from the database.

note: all of these functions arent thought out that well and theres better ways to do them
it should be more modular in logic so that the data being sent in can be in any shape and the sql
query will be generated accordingly, as of now these are simple implementations of what needs to be done
'''

#INIT CONNECTION TO DATABASE
db = c.Connect()

def data_GET(tablename):
    sql = f"SELECT * FROM {tablename}"
    return db.select_query(sql)


def data_INSERT(tablename, columns, data):
    sql = f"INSERT INTO {tablename}({columns} VALUES ({data}))"
    db.execute(sql)

def data_UPDATE(tablename, column_new, data_new, column_old, data_old):
    sql = f"UPDATE {tablename} SET {column_new} = {data_new} WHERE {column_old} = {data_old}"
    db.execute(sql)

def data_DELETE(tablename, column, value):
    sql = f"DELETE FROM {tablename} WHERE {column} = {value}"
    db.execute(sql)

    
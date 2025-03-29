import oracledb

def get_connection():
    connection = oracledb.connect(
        user='pawel',
        password='rootuser1',
        dsn='localhost:1521/XEPDB1'
    )
    return connection

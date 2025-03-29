""""
DATABASE CONNECTION WITH ORACLE 
------------------------------------------------
from flask import Flask, jsonify, request
import oracledb

app = Flask(__name__)

# Function to create Oracle database connection
def get_connection():
    connection = oracledb.connect(
        user='pawel',
        password='rootuser1',
        dsn='localhost:1521/XEPDB1'
    )
    return connection"

--------------------------


    """
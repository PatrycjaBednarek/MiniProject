import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="test"
)

cursor = connection.cursor()

cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()
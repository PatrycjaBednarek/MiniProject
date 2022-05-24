import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mini_project"
)

cursor = connection.cursor()
cursor.close()

def view_items(table_name):
    cursor = connection.cursor()
    sql = f"SELECT * FROM {table_name}"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    return results


def retrieve_result(query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results


def insert_or_update(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
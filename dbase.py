# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import OperationalError
from config import host, user, password, database, port

def create_connection(dbname, dbuser, dbpassword, dbhost, dbport):
    connection = None
    try:
        connection = psycopg2.connect(
            database=dbname,
            user=dbuser,
            password=dbpassword,
            host=dbhost,
#            port=dbport
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(r"The error '{e}' occurred")
    return connection

def create_table():
    connection = create_connection(database, user, password, host, port)
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        insert_query = "DROP TABLE IF EXISTS apartments_info;"
        insert_query2 = """CREATE TABLE apartments_info(
                    id SERIAL PRIMARY KEY,
                    cost INT,
                    title VARCHAR,
                    url VARCHAR);"""
        cursor.execute(insert_query)
        cursor.execute(insert_query2)
        connection.commit()
    connection.close()

def add_row(data_row):
    connection = create_connection(database, user, password, host, port)
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        insert_query = ("""INSERT INTO apartments_info(cost, title, url)
                    VALUES(%s);""" % data_row)
        cursor.execute(insert_query)
        connection.commit()
    connection.close()

# ToDo функция которая распечатывает все строки из таблицы (пока cost, title и url) в которых значение cost меньше и\или
#  больше указанной величины
def cost_sorting(min_cost, max_cost):
    connection = create_connection(database, user, password, host, port)
    cursor = connection.cursor()
    # сортировка данных по cost
    with connection.cursor() as cursor:
        sorting_query1 = ("""SELECT * 
                        FROM apartments_info
                        WHERE cost BETWEEN %s
                        ORDER BY cost DESC;""" % (str(min_cost)+' AND '+str(max_cost)))
        cursor.execute(sorting_query1)
        connection.commit()
        return cursor.fetchall()
        # for row in table_name:
        #     x = row
        #     print(row)
    connection.close()

def print_table():
    connection = create_connection(database, user, password, host, port)
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        insert_query = ("""SELECT * FROM apartments_info;""" )
        cursor.execute(insert_query)
        rows = cursor.fetchall()
        connection.commit()
    connection.close()
    return rows

#create_table()
#cost_sorting(3000000, 4000000)
#print_table()
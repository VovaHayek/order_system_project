import mysql.connector
from mysql.connector import Error

from decouple import config

def get_data_from_database():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='service',
                                            user='root',
                                            password=config('PASSWORD'))
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()

            data = {}
            get_order_data = connection.cursor()
            cursor.execute('select * from homepage_order;')
            order_db_data = cursor.fetchall()

            get_order_menu_data = connection.cursor()
            cursor.execute('select * from homepage_order_dishes;')
            order_dish_db_data = cursor.fetchall()

            for index, restaurant_id, amount in order_db_data:
                data[index] = {'restaurant': restaurant_id}
                data[index].update({'amount': amount})
                data[index].update({'menu': []})
            for index, order_id, food_id in order_dish_db_data:
                data[order_id]['menu'].append(food_id)

            return data

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
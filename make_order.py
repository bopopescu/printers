import mysql.connector
import pandas as pd
from mysql.connector import Error


def connect(database):
    try:
        if database.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)


def get_query(string, sqlbase):
    cursor = sqlbase.cursor()
    cursor.execute(string)
    result = cursor.fetchall()
    return result


if __name__ == '__main__':
    db = mysql.connector.connect(host='localhost',
                                 database='printers',
                                 user='root',
                                 password='root',
                                 port='8889')
    connect(db)
    query = ('SELECT CEILING(COUNT(events.id)/3), name FROM events \n'
             '    JOIN consumables ON consumable_id=consumables.id \n'
             '    WHERE date > LAST_DAY(CURDATE()) + INTERVAL 1 DAY - INTERVAL 3 MONTH \n'
             '    AND date < DATE_ADD(LAST_DAY(CURDATE()), INTERVAL 1 DAY) \n'
             '    GROUP BY name')
    rows = get_query(query, db)
    data = pd.DataFrame(data=rows, columns=['Необходимо', 'Модель'])
    print(data)
    data.to_excel('order.xlsx', sheet_name='sheet_1', index=False)
    db.close()


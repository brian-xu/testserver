import json
import threading

import pymysql.cursors


class SQLHandler(object):
    def __init__(self):
        self.insert_queue = threading.Semaphore()
        self.insert_conn = self.connection()

    def connection(self) -> pymysql.Connection:
        return pymysql.connect(host='localhost',
                               user='root',
                               passwd='',
                               db='test')

    def threaded_select(self):
        connection = self.connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `test_table` ORDER BY id DESC LIMIT 6")
            messages = cursor.fetchall()
            cursor.close()
        connection.close()
        return json.dumps(messages)

    def threaded_insert(self, content):
        with self.insert_conn.cursor() as cursor:
            cursor.execute("""INSERT INTO `test_table` (`id`, `name`) 
                                 VALUES (%s, %s)""", (0, content))
            cursor.close()
        self.insert_conn.commit()
        self.insert_queue.release()

    def submit(self, content):
        self.insert_queue.acquire()
        self.threaded_insert(content)

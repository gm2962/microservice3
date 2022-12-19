import os
import pymysql

class OrdersResource:
    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        return conn


    @staticmethod
    def get_orders():
        sql = f"SELECT * FROM commerce3.orders"
        conn = OrdersResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = list(cur.fetchall())
        return result

    @staticmethod
    def get_order_by_id(key, val="*"):

        sql = f"SELECT {val} FROM commerce3.orders where order_id='{key}'"
        conn = OrdersResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = list(cur.fetchall())

        return result
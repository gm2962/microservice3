import os
import pymysql

class ProductsResource:
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
        sql = "SELECT * FROM commerce3.products"
        conn = ProductsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = list(cur.fetchall())

        return result

    @staticmethod
    def get_product_by_id(key):

        sql = f"SELECT * FROM commerce3.products where product_id='{key}'"
        conn = ProductsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchone()

        return result
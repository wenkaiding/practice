import pymysql

__author__ = 'martin'


class Demo():
    def __init__(self):
        self.connection = pymysql.connect(host="",
                                          user="",
                                          port=,
                                          password="",
                                          db="",
                                          charset='')
        self.db = None

    def dbconnecter(self):
        with self.connection.cursor() as cursor:
            cursor.execute("")
            query_result = cursor.fetchall()
            # TODO catch exception
        print query_result[1][0]


if __name__ == '__main__':
    demo = Demo()
    demo.dbconnecter()

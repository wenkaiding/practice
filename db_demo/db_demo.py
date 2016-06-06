import pymysql

__author__ = 'martin'


class Demo():
    def __init__(self):
        self.connection = pymysql.connect(host="",
                                          user="",
                                          password="",
                                          db="",
                                          charset='utf8')
        self.db = None

    def dbconnecter(self):
        with self.connection.cursor() as cursor:
            self.connection.cursor().execute("select id from ### limit 100")
            query_result = cursor.fetchall()
            # TODO catch exception
        print query_result


if __name__ == '__main__':
    demo = Demo()
    demo.dbconnecter()

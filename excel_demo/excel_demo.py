# coding:utf-8
__author__ = 'martin'


from xlrd import open_workbook
from xlutils.copy import copy

class create_excel():

    def __init__(self):
        pass

    def demo(self):
        rb = open_workbook("/Users/martin/Desktop/1w.xslx")
        rs = rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        temp = 0
        tmp = 0
        for i in range(5000):
            temp += 1
            if temp/100000 == 1:
                print temp
                print tmp
                temp = 0
                tmp += 1
                print temp
            ws.write(i, tmp, i)
        wb.save("/Users/martin/Desktop/1w.xslx")
        print "pass"





if __name__ == '__main__':
    create_excel().demo()

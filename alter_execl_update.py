import xlrd
from xlutils.copy import copy #倒模块
book1 = xlrd.open_workbook('shell.xls') #打开要修改的excel
book2 = copy(book1) #拷贝一份原来的excel
sheet = book2.get_sheet(0) #获取第几个sheet页
sheet.write(1,3,0) #写入需要修改的行、列及修改后的值
sheet.write(1,0,'小黑')
book2.save('shell.xls')
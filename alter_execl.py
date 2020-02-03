import xlrd
from xlutils.copy import copy #倒模块
def alter_data(filename,sheet_namber,val):
        book1 = xlrd.open_workbook(filename) #打开要修改的excel
        book2 = copy(book1) #拷贝一份原来的excel
        sheet = book2.get_sheet(sheet_namber) #获取第几个sheet页
        m=0
        for i in range(len(val)):
                sheet.write(m,0,val[i])
                m=m+1
        book2.save(filename)
def read_data(filenmae1,sheet_name):
        file=xlrd.open_workbook(filenmae1)
        sheet_file=file.sheet_by_name(sheet_name)
        nrows = sheet_file.nrows       #行数
        ncols = sheet_file.ncols       #列数
        m=0
        M=[]
        for r in range(nrows):
                r_value = sheet_file.row_values(r)
                c_value=r_value[0]       #获取第几行的指定列值输出
                M.append(c_value)
        m=m+1
        print(M)
        alter_data('shell.xls',0,M)
read_data('end.xls','sheet')

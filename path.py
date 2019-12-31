import os
import xlrd
import xlwt

filename_end = '事件及服务记录表-钟奇.xls'
file2=xlwt.Workbook(filename_end)
sheet1 = file2.add_sheet(u'sheet1',cell_overwrite_ok=True)

a = 'C:/Users/10581/OneDrive/创立-电信枢纽/周报/新建文件夹'
dir=os.listdir(a)

m=0

for file in dir:
    print(a+'/'+file)
    filename=(a+'/'+file)
    file = xlrd.open_workbook(filename)
    try:
        sheet=file.sheet_by_name("3.1-3.5")
    except :
        sheet=file.sheet_by_name("10.8-10.12")
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    for r in range(nrows):
        row_value = sheet.row_values(r)   #获取第r行
        j = 0
        for i in row_value:
            sheet1.write(m,j,i) #循环写入 竖着写，对应x(向下)y(向左)z(赋值)
            j=j+1
        m=m+1
file2.save(filename_end)
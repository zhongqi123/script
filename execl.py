import xlrd
import xlwt
filename = '事件及服务记录表-钟奇(0923-0927).xlsx'
filename1 = '事件及服务记录表-钟奇(1008-1012).xlsx'
filename_end = '事件及服务记录表-钟奇.xls'
file = xlrd.open_workbook(filename)
sheet=file.sheet_by_name("3.1-3.5")
nrows = sheet.nrows
ncols = sheet.ncols
print(nrows)
'''
file2=xlwt.Workbook(filename_end)
sheet1 = file2.add_sheet(u'sheet1',cell_overwrite_ok=True)
m=0
for r in range(nrows):
    row_value = sheet.row_values(r)   #获取第r行
    j = 0
    for i in row_value:
        sheet1.write(m,j,i) #循环写入 竖着写，对应x(向下)y(向左)z(赋值)
        j=j+1
    m=m+1
file2.save(filename_end)
'''
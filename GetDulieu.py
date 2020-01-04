import xlrd
import os

address=os.getcwd()+"/ex1.xlsx"
list1=[];
list2=[];
list3=[]
dictionary=dict()
book=xlrd.open_workbook(address)
for i in range(book.nsheets):
	first= book.sheet_by_index(i)
	for rows in range(first.nrows):
		tienganh= first.cell_value(rows,0)
		list1.append(tienganh)
		tiengviet=first.cell_value(rows,1)
		tiengviet=tiengviet.encode('utf-8')
		list2.append(tiengviet)
		dictionary[tiengviet]=tienganh
		list3.append(0)

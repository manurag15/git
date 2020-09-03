import sqlite3
import csv

comm = sqlite3.connect('database_2.1.db')
c = comm.cursor()

c.execute('create table data(vouchergroupid,transactiondatetime)')

with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'rt') as f:
    dr = csv.DictReader(f)
    to_db = [(i['vouchergroupid'],i['transactiondatetime']) for i in dr]

c.executemany("insert into data(vouchergroupid,transactiondatetime) values(?,?);",to_db)

c.execute("select vouchergroupid,group_concat(transactiondatetime) from data group by vouchergroupid")

output = c.fetchall()

dict={}
for item in output:
    dict[item[0]] = [0]*24
    dates = item[1].split(',')
    hours = map(lambda x:int(x[12:14]),dates)
    for value in hours:
        dict[item[0]][value]+=1


# print(dict)

with open("assignment_2.1.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["VoucherGroupId"]+[f'Hour {i}' for i in range(1,25)])
    for key in dict.keys():
        writer.writerow([key]+[item for item in dict[key]])
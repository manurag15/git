import sqlite3
import csv

with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'r') as f:
    dr = csv.DictReader(f)
    to_db = [(i['vouchergroupid'],i['transactionAmount']) for i in dr]

    conn = sqlite3.connect("database_2.3.db") 
    cursor = conn.cursor()

    cursor.execute("create table t(vouchergroupid,transactionAmount)")
    cursor.executemany("insert into t(vouchergroupid,transactionAmount) values(?,?);",to_db)

    cursor.execute("select vouchergroupid,count(vouchergroupid),sum(transactionAmount) from t group by transactionAmount")
    # print(cursor.fetchall())

    with open("assignment_2.3.csv",'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['vouchergroupid','count()','sum(transactionAmount)'])
        for item in cursor.fetchall():
            writer.writerow([item[0],item[1],item[2]])


# java, frontend- angular, 
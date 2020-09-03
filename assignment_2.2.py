import csv
import sqlite3


with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'r') as f:
    dr = csv.DictReader(f)
    # print(list(dr)[0])
    to_db = [(i['serviceclassid'], i['vouchergroupid'],i['transactionAmount']) for i in dr]
    
    con = sqlite3.connect("database_2.2.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE t (serviceclassid, vouchergroupid,transactionAmount);")

    cur.executemany("INSERT INTO t (serviceclassid, vouchergroupid,transactionAmount) VALUES (?, ?,?);", to_db)
    con.commit()
    # con.close()

    # cur.execute("select * from t")
    # print(cur.fetchall())

    cur.execute("select serviceclassid,vouchergroupid,count(vouchergroupid),sum(transactionAmount) from t group by serviceclassid,vouchergroupid")
    
    # print(type(cur.fetchall()))
    data = cur.fetchall()

with open("assignment_2.2.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['serviceclassid','vouchergroupid','count()','sum(transactionAmount)'])
    for item in data:
        writer.writerow([item[0],item[1],item[2],item[3]])




    
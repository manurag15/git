import csv

with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'rt') as f:
    data = list(csv.reader(f))
    data_list = [data[i][:] for i in range(1,len(data)-1)]

dict = {}

for entry in data_list:
    key = entry[4]
    transaction_amount = entry[6]

    if key not in dict.keys():
        dict[key] = [0,0]

    dict[key][0]+=1
    dict[key][1] += float(transaction_amount)

# print(dict)

with open('assignment_1.3.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['vouchergroupid','count()','sum(transactionAmount)'])
    for key in dict.keys():
        writer.writerow([key,dict[key][0],dict[key][1]])
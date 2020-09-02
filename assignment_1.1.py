import csv


with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'rt') as f:
    data = list(csv.reader(f))
    data_list = [data[i][:] for i in range(1,len(data)-1)]
    # print(data_list)

dict = {}





for item in data_list:
    key = item[4]
    time = int(item[5][12:14])
    if key not in dict.keys():
        dict[key]=[0]*24

    dict[key][time]+=1

# print(dict)

with open("assignment_1.1.csv",'w',newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(["VoucherGroupId","Hour 1","Hour 2","Hour 3","Hour 4","Hour 5","Hour 6","Hour 7","Hour 8","Hour 9","Hour 10","Hour 11","Hour 12","Hour 13","Hour 14","Hour 15","Hour 16","Hour 17","Hour 18","Hour 19","Hour 20","Hour 21","Hour 22","Hour 23","Hour 24"])
    writer.writerow(["VoucherGroupId"]+[f'Hour {i}' for i in range(1,25)])
    for key in dict.keys():
        writer.writerow([key]+[item for item in dict[key]])

        
    
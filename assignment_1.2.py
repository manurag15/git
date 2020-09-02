import csv
import itertools

# svId_arr = []
# vId_arr = []


with open("05_KOL_BH_PYMT_STATIC_20200819.txt",'rt') as f:
    data = list(csv.reader(f))
    data_list = [data[i][:] for i in range(1,len(data)-1)]
    



dict = {}


out = itertools.groupby(data_list,lambda x:x[3])

for key,group in out:
    out_2 = itertools.groupby(group,lambda x:x[4])
    with open("assignment_2_output.csv",'w') as file:

        for key1,group1 in out_2:
            if (key,key1) not in dict.keys():
                dict[(key,key1)] = [0,0]
            
            for item in group1:
                dict[(key,key1)][0]+=1
                dict[(key,key1)][1]+= float(item[6])

# print(dict)

# write to file

with open('assignment_1.2.csv' ,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['serviceclassid','vouchergroupid','count()','sum(transactionAmount)'])
    for key in dict.keys():
        writer.writerow([key[0],key[1],dict[key][0],dict[key][1]])


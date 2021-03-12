# from collections import defaultdict
# import csv

# def pm_dict(filename):
#     D = defaultdict(int)
#     with open(filename, 'r', newline='\n') as f:
#         r = csv.reader(f)
#         for key,value in r:
#             D[key] += float(value)
#     f.close()
#     with open(filename,'w') as ff:
#         for i in D.keys():
#             ff.write('{} {}\n'.format(i, D[i] * 0))
#     ff.close()
#     return dict(D) # converts back to a standard dict, but not required.

# print(pm_dict('outputLog/080tokens.txt'))

with open("outputLog/493tokens.txt", "r") as file:
    rows = ( line.split(',') for line in file)
    dict = { row[0]:row[1] for row in rows }
for item in dict:
    print(item," ",dict[item])
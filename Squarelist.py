import math
import csv

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    g=len(data)
    total=0
    for h in data:
        total+=int(h)
    mean=total/g
    return mean 

squarelist=[]
for k in data:
    m=int(k)-mean(data)
    m=m**2
    squarelist.append(m)

sum=0
for b in squarelist:
    sum=sum+b
result=sum/(len(data)-1)
j=math.sqrt(result)
print(j)

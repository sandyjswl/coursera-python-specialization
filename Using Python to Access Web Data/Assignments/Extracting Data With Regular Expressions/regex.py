import re
fh=open('data.txt')
res=[]
for line in fh:
    temp=re.findall('[0-9]+',line)
    for i in temp:
        res.append(i)
for i in range(len(res)):
    res[i]=int(res[i])
print(sum(res))

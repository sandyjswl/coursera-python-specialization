name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
res={}
for line in handle:
    temp_list=[]
    if line.startswith('From'):
        temp_list=line.split()
        res[temp_list[1]]=res.get(temp_list[1],0)+1
maximum=res.values()
max_val=max(maximum)
for i,j in res.items():
    if j==max_val:
        print(i,str(int(j/2)))
            
        
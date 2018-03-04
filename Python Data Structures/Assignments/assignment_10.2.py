name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
res={}
for line in handle:
    if line.startswith('From'):
        tmp_list=line.split()
        if(len(tmp_list))>3:
            tmp_time=tmp_list[5]
            time=tmp_time.split(':')
            res[time[0]]=res.get(time[0],1)+1
for k,v in sorted(res.items()):
    print(k,str(int(v-1)))
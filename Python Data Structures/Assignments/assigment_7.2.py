# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
values=[]
count=0
result=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        count+=1
        f_val=line.find('0')
        values.append(float(line[f_val:]))
for val in values:
    result=result+val
print("Average spam confidence: "+str(result/len(values)))
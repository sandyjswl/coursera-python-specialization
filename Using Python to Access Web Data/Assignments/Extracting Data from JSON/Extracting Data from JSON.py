import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

url = input("Enter location: ")
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info=json.loads(data)
result=0
count=0
#print(info)
for item in info["comments"]:
	result=result+int(item['count'])
	count=count+1
print('Counts: ',count)	
print(result)	

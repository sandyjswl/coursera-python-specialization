# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input("Enter count: "))
pos=int(input('Enter position: '))
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#count=0
#for tag in range(len(tags)):
#    print(tags[2].get('href', None))
    
for i in range(1,count+1):
    if i==1:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        print("Retreiving: ",url)
        print("Retreiving: ",tags[pos-1].get('href', None))
        url=tags[pos-1].get('href', None)
    else:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        
        print("Retreiving: ",tags[pos-1].get('href', None))
        url=tags[pos-1].get('href', None)

        

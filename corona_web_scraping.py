import requests
import re
from bs4 import BeautifulSoup

print("Enter the country for which you want to find Corona Cases : ")
ur=input()
new_url=("https://www.worldometers.info/coronavirus/country/"+ur)
new_page = requests.get(new_url)
new_page=new_page.text

l1=[]
new_soup = BeautifulSoup(new_page, "html.parser" )
b = new_soup.findAll("h1")

for i in b:
    y=i.text
    fin2 = "".join(re.split("[^a-zA-Z]*", y))
    l1.append(fin2)
    
d={}
c = new_soup.findAll("div", {"class":"maincounter-number"})
inc=1

for i in c:
        
    z=i.text
    fin3 = str(re.sub("\D", "", z))
    d[l1[inc]]=fin3
    inc+=1
    
print(l1[0],"Cases :")    
for x, y in d.items():
    print(x,":", y)
    
url="https://www.worldometers.info/coronavirus/"
page = requests.get(url)
page=page.text
        
soup = BeautifulSoup(page, "html.parser" )
a =soup.findAll("div", {"class":"maincounter-number"})
d={}
inc=1

for i in a:        
    x=i.text
    final = str(re.sub("\D", "", x))
    d[l1[inc]]=final
    inc+=1  
    
print("\nWorldwide Cases :")
for x, y in d.items():
    print(x,":", y)

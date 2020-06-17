#%%
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
    res1 = "".join(re.split("[^a-zA-Z]*", y))
    l1.append(res1)
    
d={}
c = new_soup.findAll("div", {"class":"maincounter-number"})
j=1

for i in c:
        
    z=i.text
    res = str(re.sub("\D", "", z))
    d[l1[j]]=res
    j+=1
    
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
    


#%%
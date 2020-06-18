import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.nationsonline.org/oneworld/countries_of_the_world.htm"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

Countries=[]

My_table = soup.findAll("a")
for i in My_table:
    b = i.text.replace('\n', ' ').strip()
    Countries.append(b)

del Countries[0:83]
del Countries[-24:]
Countries[-13]="UK"
Countries[-12]="USA"
    
print("Enter the country for which you want to find Corona Cases : ")
ur=input()
if ur in Countries:
    new_url=("https://www.worldometers.info/coronavirus/country/"+ur)
    new_page = requests.get(new_url)
    new_page=new_page.text
    
    l1=[]
    new_soup = BeautifulSoup(new_page, "html.parser" )
    b = new_soup.findAll("h1")
    
    for i in b:
        l1.append(i.text.replace('\n', ' ').strip())
        
    d={}
    c = new_soup.findAll("div", {"class":"maincounter-number"})
    inc=1
    
    for i in c:
        #for removing the extra characters apart from the main headings
        fin3 = i.text.replace('\n', ' ').strip()
        d[l1[inc]]=fin3
        inc+=1
          
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
        final = i.text.replace('\n', ' ').strip()
        d[l1[inc]]=final
        inc+=1  
        
    print("\nWorldwide Cases :")
    for x, y in d.items():
        print(x,":", y)
else:
    print("Anything entered other than country's name will not be taken into consideration")
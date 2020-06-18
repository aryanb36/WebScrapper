import requests
from bs4 import BeautifulSoup

world_url="https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

html_content = requests.get(world_url).text
world_soup = BeautifulSoup(html_content, "lxml")

My_table = world_soup.find('table',{'class':'sortable'})

links=My_table.findAll('a')

Countries = []
for each_country in links:
    Countries.append(each_country.get('title'))
    
coun = print("Enter the country for which you want to find Corona Cases : ")
if (coun not in Countries):
    print("Enter Countries Only please")
else:
    ur=input()
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
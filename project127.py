from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
starTable=soup.find('table')
temp_list=[]
tableRows=starTable.find_all('tr')
for tr in tableRows: 
    td=tr.find_all('td')
    row=[i.text.rstrip( for i in td)]
    temp_list.append(row)
starName=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range(1,len(temp_list)): 
    starName.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df=pd.DataFrame(list(zip(starName,distance,mass,radius,lum)),columns=['Star Name','Distance','Mass','Radius','Luminosity'])
print(df)
df.to_csv('brightStars.csv')
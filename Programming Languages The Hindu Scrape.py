import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

#This portion is for Introduction

print("                Programming Languages Lab Project                   ")
print()
print()
print("This is a project made by: Shivam Jha, Deepanshu Jain, Nikhil Swami.")
print("The project is being submitted to: prof.Rajiv Ratn Shah")
print("This project's function is to scrape data from The Hindu's online site.")
print("The category of Articles whose data is benig scraped is: Technology and Sciences.")
print("All the Data which has been scraped has been stored in the JSON format")
print()
print()


#This portion is for Headings and Date of Publish
my_url = 'https://www.thehindu.com/sci-tech/technology/'
page_soup = soup(uReq(my_url).read(),"html.parser")
 
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]

headings=page_soup.findAll("h3")
for i in range (0,len(page_soup.findAll("h3"))):
    try:
        l1.append(headings[i].text)
        l2.append(headings[i].a['title'])
    except:
        print()
s1=json.dumps(l1,indent=4)
with open('l1.json','w') as f1:
    json.dump(s1,f1)
print("This is the list for all the Headings of Articles on the Home page:")
print()
print(s1)
print()
s2=json.dumps(l2,indent=4)
with open('l2.json','w') as f2:
    json.dump(s2,f2)
print()
print()
print("This is the list for all the Dates of Articles on the Home page:")      
print()
print(s2)
print()

#This portion is for Sources of all the Articles
 
for i in range (0,len(page_soup.findAll("h3"))):
    try:
        l3.append(headings[i].a['href'])
    except:
        print('')  
s3=json.dumps(l3,indent=4)
with open('l3.json','w') as f3:
    json.dump(s3,f3)
print("This is the list of all the sources of the Articles:")
print()
print(s3)  
print()
print()

#This portion is for the Text Content of the articles

for j in range(len(l3)):
    my_url = requests.get(l3[j]).text
    soup = BeautifulSoup(my_url,"lxml")
    s=soup.find_all('p')
    for i in range(len(s)):
        l4.append(s[i].text)
s4=json.dumps(l4,indent=4)
with open('l4.json','w') as f4:
    json.dump(s4,f4)
print("This is the list of all Text Content of the Articles: ")
print()
print(s4)
print()

#This portion is for Image source URL
for i in range(len(l3)):
    my_url = requests.get(l3[i]).text
    soup = BeautifulSoup(my_url,"lxml")
    link = soup.find_all('img')
    print('This img belongs to '+l3[i]+' link')
    for j in range(len(link)):
        l5.append(link[j]['src'])
    s5=json.dumps(l5,indent=4)
    with open('l5.json','w') as f5:
        json.dump(s5,f5)
    print()
    print(s5)

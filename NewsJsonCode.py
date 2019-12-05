from bs4 import BeautifulSoup as soup
import json
import threading
import requests
import html5lib
import time

def checker(needle,haystack):
    return needle in haystack

# parallalization speed
parallel=8

#Recource Declaration
my_url = 'https://www.thehindu.com/sci-tech/technology/?page=1'

#global-variables
string=''
pageno=[]

#holder for thread data
threadsync=[]
threaddata=[]

for r in range (parallel):
    threaddata.append([])


#Page index generator
for i in range (0,216):
    string='https://www.thehindu.com/sci-tech/technology/?page='+str(i+1)
    pageno.append(string)

#gets page 1 to n and their contents
def worker(a,b,t_index):
    locallist1=[]
    locallist2=[]
    locallist3=[]
    localpara =[]
    eachpost=[]

    for j in range( a,b):
        #get soup in html format of current page index
        raw_data=requests.get(pageno[a]).content
        page_soup = soup(raw_data,'html5lib')

        headings=page_soup.findAll("h3") 
        #Headings and relavant content Scanner for current page index and store in list
        for i in range (14,len(page_soup.findAll("h3"))):   
            #error and exception handler block
            try:
                month_filter=['dec','nov','oct']
                dates=headings[i].a['title']
                for x in range( len(month_filter) ):
                    if (checker (month_filter[x] , dates.lower() ) == True):
                        print(month_filter[x],'present') 
                        
                        locallist1.append(headings[i].text)
                        locallist2.append(dates)
                        locallist3.append(headings[i].a['href'])
                    
                    else :
                        pass
            except:
                print("entry",i,'of page',j,'not found');
                locallist1.append('entry not found');
                locallist2.append('entry not found');
                locallist3.append('entry not found');

        for k in range(len(locallist3)):
            lest=''
            try: 
                sub_soup=requests.get( locallist3[k] ).content
                link_soup=soup(sub_soup,"html.parser")
                container=link_soup.find_all('p');
                for l in range(len(container)-8):
                    lest=lest+container[l].text
                localpara.append(lest)
                print('thread',t_index ,'Completion',( round(k*100/len(locallist3)) ),'%' )
            except:
                print('error')
                localpara.append('couldnt find the paragraph')
                    
  
      #join and merge resources with main
    for sync in range(len(locallist1)):
        eachpost.append([])
        eachpost[sync].append(locallist1[sync])
        eachpost[sync].append(locallist2[sync])
        eachpost[sync].append(locallist3[sync])
        eachpost[sync].append(localpara[sync])
        
    
    threaddata[t_index-1].extend(eachpost)
    

    
                        


#Thread Parallalisation block
thread_spool=[]

for i in range(1,parallel+1):
    thread_spool.append ( threading.Thread(target=worker,args=(i-1, i, i)) )
    thread_spool[i-1].start()


for i in range(len(thread_spool)):
    thread_spool[i].join()
    print ('thread-------',i+1,'------------joined')


for x in range(len(threaddata)):
    threadsync.extend(threaddata[x])
# print(threadsync)


#storing in JSON Usable Dictonary
allinfo={'Posts':threadsync,}

#OPTIONAL : viewing of content
# print(json.dumps(allinfo,indent=4))

#print(threadsync)
with open('newspost.json','w') as f1:
    json.dump(allinfo,f1,indent=2 )


'''#\n correction  for list 1 to increase readability
lst1=[]
for i in range(len(l1)):
    lst1.append(l1[i].replace('\n',''))'''


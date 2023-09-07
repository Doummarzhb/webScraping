import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]
salary=[]
responsibilities=[]

result= requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

src=result.content
# print(src)

soup=BeautifulSoup(src,"lxml")
# print(soup)

#eza habin ndawer 3al ma3lomet le bdna te3 safha b2lb wuzzuf 
job_titles=soup.final_all("h2",{"class":"css-nn640qf"} )
company_names=soup.find_all("a",{"class":"css-17s97q8"})
locations_names=soup.find_all("span",{"class":"css-5wys0k"})
jo_skills=soup.find_all("div",{"class":"css-y4udm8"})


# step loop over returned lists to extract needed info into other lists 

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(locations_names[i].text)
    skills.append(jo_skills[i].text)


for link in links:
    result=requests.get(link)
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    salaries=soup.find_all("div",{"class":"matching-requirement-icon-container","data-toggle":"tooltip","data-placement":"top"})
    salary.append(salaries.text.strip())
    requirements=soup.find("span",{"itemprop":"responsibilities"}).ul
    respon_test=""
    for li in requirements.fin_all("li"):
        respon_test +=li.test+" | "
    responsibilities.append(respon_test)

# print(company_name,location_name)

#step create csv file and fill hon mnchn lfille enu wen mawjod 3al computer
# w enu chuf chu bdu yetnafas be 2alb file fhmto ?
file_list=[job_title,company_name,location_name,skills,links,salary]
exported=zip_longest(*file_list) #empacing be fade heye hayde *
with open("/Users/doummar/documents/jobstext.csv","w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["job title","company name", "location","skills","links","salary"]) #awal row le mawjoden bel file 
    wr.writerows(exported)
    

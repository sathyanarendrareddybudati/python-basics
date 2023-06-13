from bs4 import BeautifulSoup
import requests
import time
# with open('aboutme.html', 'r') as file:
#     a=file.read()
#     soup = BeautifulSoup(a,'html.parser')
#     # print(soup.prettify())
#     b = soup.findAll('div', class_='bv')
#     for i in b:
#         f = i.p.text
#         print(f)
print('put some skills you are not familer with')
unfamilier = input('>')
print(f'filtering out {unfamilier}')
def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    jobs_1 = requests.get(url).text
    soup = BeautifulSoup(jobs_1,'html.parser')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published = job.find('span',class_='sim-posted').text
        if 'few' in published:
            find = job.find('h3',class_='joblist-comp-name').text
            pvt = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            # print(more_info)
            if unfamilier not in pvt:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'find :{find.strip()} \n')
                    f.write(f'skills :{pvt.strip()} \n')
                    f.write(f'more_info :{more_info}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} mintues...')
        time.sleep(time_wait * 60)
         



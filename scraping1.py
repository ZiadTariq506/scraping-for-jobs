from bs4 import BeautifulSoup
import requests
import time
import os
import glob


def find_jobs():
    files = glob.glob('saved_jobs/*')
    for file in files:
        os.remove(file)
    # A
    print('Write unfamiliar skill (let it blank if it none):')
    unfamiliar_skill = input('>')
    # B
    print('Write a familiar skill (let it blank if it none):')
    familiar_skill = input('>')
    # C
    print('what is the job u looking for are about(ex: linux, bash, python scraping):')
    Search_For = input('>')
    Search_For_edited = Search_For.replace(' ', '+')

    print("Searching... :)")
    html_site_text = requests.get(
        f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
        f'=submit&txtKeywords={Search_For_edited}&txtLocation=').text
    soup = BeautifulSoup(html_site_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date or '1' in published_date or '2' in published_date or '3' in published_date:
            company = job.find('h3', class_='joblist-comp-name').text.replace('(More Jobs)', '').replace('    ', '')
            skills = job.find('span', class_='srp-skills').text.replace('  ', ' ')
            # to get the argument href
            more_info = job.header.h2.a['href']

            def save_job():
                with open(f'saved_jobs/{index}.txt', 'w') as s:
                    s.write(f'Company Name: {company.strip()} \n')
                    s.write(f'Required Skills: {skills.strip()} \n')
                    s.write(f'More Info: {more_info} \n')

            # cases for the familiar and unfamiliar skills
            # A
            if unfamiliar_skill not in skills and familiar_skill in skills:
                # use strip() remove the additional spaces and blanks
                print(f'Company Name: {company.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'More Info: {more_info}')
                save_job()
                print('\n')
            # A
            elif unfamiliar_skill == "" and familiar_skill in skills:
                print(f'Company Name: {company.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'More Info: {more_info}')
                save_job()
                print('\n')

            elif unfamiliar_skill not in skills and familiar_skill == "":
                print(f'Company Name: {company.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'More Info: {more_info}')
                save_job()
                print('\n')

            elif unfamiliar_skill == "" and familiar_skill == "":
                print(f'Company Name: {company.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'More Info: {more_info}')
                save_job()
                print('\n')
    print("Do You Want To Save The Listed Jobs[y/n]:")
    save_the_jobs = input('>')
    if save_the_jobs == 'n' or save_the_jobs == 'no':
        files = glob.glob('saved_jobs/*')
        for file in files:
            os.remove(file)
    elif save_the_jobs == 'y' or save_the_jobs == 'yes':
        print('jobs have been saved!!!')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

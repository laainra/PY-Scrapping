import requests
from bs4 import BeautifulSoup as bs
import csv
import mysql.connector

URL = 'https://proxyway.com/news/page/'

titles_list = []
title_page = []

for page in range(1, 7):
    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('h3', attrs={'class': 'archive-list__title'})
    count = 1
    
    for title in titles:
        d = {}
        d['Page Number'] = f'Page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text
        titles_list.append(d)
        count += 1
    
    if page == 7:
        count = 1
        for title in titles:
            e = {}
            e['Page Number'] = f'Page {page}'
            e['Title Number'] = f'Title {count}'
            e['Title Name'] = title.text
            count += 1
            title_page.append(e)

titles_all = titles_list + title_page

filename = 'hasilScrapping.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, ['Page Number', 'Title Number', 'Title Name'])
    writer.writeheader()
    writer.writerows(titles_all)




# Connect to the database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='scrapping'
)

# Create a cursor object
cursor = connection.cursor()

# Insert the data into the database table
for title in titles_all:
    page_number = title['Page Number']
    title_number = title['Title Number']
    title_name = title['Title Name']
    query = "INSERT INTO scraped_data (page_number, title_number, title_name) VALUES (%s, %s, %s)"
    values = (page_number, title_number, title_name)
    cursor.execute(query, values)

# Commit the changes and close the connection
connection.commit()
connection.close()
print('Data saved successfully')

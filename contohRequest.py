import requests
from bs4 import BeautifulSoup



req = requests.get('https://uns.ac.id/id/')

soup = BeautifulSoup(req.content, 'html.parser')

s = soup.find('div', id='page-container')

content = s.find_all('a')
print(soup.title)
print(soup.title.name)
print(content)


# r = requests.get('https://vokasi.uns.ac.id/program-studi-2/')

# soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)

# re = requests.get('https://smartinotek.com/')

# soups = BeautifulSoup(re.content, 'html.parser')

# s = soups.find('div', class_='entry-content')

# content = s.find_all('p')

# print(content)

# print(r.url)

# print(r.status_code)

# print(r)

# print(r.content)

# req = requests.get('https://www.geeksforgeeks.org/python-programming-language/')


# soup = BeautifulSoup(req.content, 'html.parser')

# s = soup.find('div', id='main')
# leftbar = s.find('ul', class_='leftBarList')
# content = leftbar.find_all('li')

# print(content)


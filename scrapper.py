import requests
from bs4 import BeautifulSoup
import lxml

walmart_electronics_source = requests.get('https://www.walmart.com/search/?query=&cat_id=3944')
walmart_electronic_department_base = 'https://www.walmart.com/search/?cat_id=3944_'

walmart_electronics = BeautifulSoup(walmart_electronics_source, 'lxml')

department_labels = walmart_electronics.find_all('li', class_="department-single-level")

print(department_labels)
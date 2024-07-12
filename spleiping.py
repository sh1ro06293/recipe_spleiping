import requests
from bs4 import BeautifulSoup

def get_recipe(url):
    url_recpie = requests.get(url)
    bsObj = BeautifulSoup(url_recpie.text,"html.parser")
    items = bsObj.find_all("div", class_="ingredient_name")
    item_names_list = []
    for i in items:
        item_names_list.append(i.text)
    return item_names_list, url      

url ='https://cookpad.com/'

search = input('検索ワードを入力してください：')
search_url = requests.get('https://cookpad.com/search/' + search +'%20おつまみ')
bsObj = BeautifulSoup(search_url.text,"html.parser")
items = bsObj.find_all("a", class_="recipe-title")

item_url = []
item_title = []

for i in range(3):
    item_url.append(items[i].get('href'))
    item_title.append(items[i].text)

print(item_title)
title_number = int(input("どのレシピを見たいですか？1-3で入力:"))

if title_number == 1:
    print(item_title[0])
    recipe_url = url+item_url[0]
elif title_number == 2:
    print(item_title[1])
    recipe_url = url+item_url[1]
elif title_number == 3:
    print(item_title[2])
    recipe_url = url+item_url[2]
else:
    print("1-3の数字を入力してください")

recipe = get_recipe(recipe_url)
print(recipe[0])
print(recipe[1])
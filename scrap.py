# Libraries
import requests, json
from bs4 import BeautifulSoup

# Modules
from lib import htmlBuilder

## REQUESTS
url = 'https://www.dekudeals.com/'
page = requests.get(url + "hottest")
soupdata = BeautifulSoup(page.content, "html.parser")
results = soupdata.find_all("div", class_="cell")

# JSON results
games = []
count = 0

## STRUCTURE OF RESULTS 
with open("index.html", "w+", encoding="utf-8") as file:
    htmlBuilder.setTemplateStart(file)
    soup = BeautifulSoup(file, "html.parser")

    # all games
    for i,result in enumerate(results):
        name = result.find("div", class_="name").text.replace("\n", '')
        previousPrice = result.find("s", class_="text-muted")
        currentPrice = result.find("strong")
        isLowest = result.find("span", class_="badge-warning")
        discount = result.find("span", class_="badge-danger")
        picture = result.find('img')['src'] if result.find('img')['src'] else ''
        linkDetail = url + result.find('a')['href']

        # start of a row (one each three columns)
        if (i%3 == 0):
            file.write(f'''<div class="row">''')

        file.write(f'''<div class="col">
            <div class="card mb-3 mt-3">
                <h2 class="card-header">{name}</h2>
                    <a href="{linkDetail}" target="_blank"><img width=100% height=100% alt="{name}" src="{picture}"></a>
                    <ul class="list-group">
                        <li class="list-group-item">
                            <strike>{previousPrice.text}</strike>
                            <small style="float:right">{isLowest.text if isLowest else ''}</small>
                        </li>
                        <li class="list-group-item">
                            {currentPrice.text}
                            <mark style="background-color:red; color:white; float:right; border-radius:8px">{discount.text if discount else ''}</mark>
                        </li>
                    </ul>
                </div>
            </div>
            ''')
        # end of row
        if (i%3 == 2):
            file.write('</div>')

            # one game in json
            games.append(json.loads(json.dumps({"name" : name,
                "previousPrice": previousPrice.text,
                "currentPrice": currentPrice.text,
                "isLowest": isLowest.text if isLowest else '',
                "discount": discount.text,
                "picture": picture,
                "linkDetail": linkDetail,
            },
            indent = 2)))
            count += 1
    
    htmlBuilder.setTemplateEnd(file)

# CREATE JSON
with open("db.json", "w", encoding="utf-8") as gamesFile:
    gamesFile.write(json.dumps({
        "count" : count,
        "results": games
    }, indent=2))

print('Scrapping Complete !')
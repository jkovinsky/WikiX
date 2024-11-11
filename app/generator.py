import requests
import wikipediaapi
import random

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

WIKI_WIKI = wikipediaapi.Wikipedia('MyProjectName randomwikiwalk@gmail.com)', 'en')


def getRandomCategory():
    params = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "5"
    }
    category_found = False
    while not category_found: 
        request = S.get(url=URL, params=params)
        data = request.json()
        randoms = data["query"]["random"]
        for r in randoms:
            if 'Category' in r["title"]:
                category_found = True
                return r["title"].split(":")[1]

def getCategoryMembers(categorymembers, level=0, max_level=1):
    members = []
    for c in categorymembers.values():
        members.append(c)
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            return getCategoryMembers(c.categorymembers, level=level + 1, max_level=max_level) 
    return members

def getValidMembers(members):
    valid_articles = []
    for member in members:
        if member.ns == wikipediaapi.Namespace.MAIN:
            valid_articles.append(member.title)
    
    return valid_articles

def getPages():
    category = getRandomCategory()

    cat = WIKI_WIKI.page(f"Category:{category}")

    catMembers = getCategoryMembers(cat.categorymembers)

    pages = getValidMembers(catMembers)

    return pages


def fetchPage():

    pages = getPages()
    content = {'title': None, 'summary' : None, 'url' : None}
    page_found = False
    count = 0

    while not page_found:

        if not pages:
            pages = getPages()

        else:
            random_page  = random.choice(pages)

            page = WIKI_WIKI.page(f'{random_page}')

            if count == len(pages):
                pages = getPages()

            if page.exists():

                if len(page.summary) > 0:

                    content['title']   = page.title
                    content['summary'] = page.summary
                    content['url']     = 'https://en.wikipedia.org/wiki/' + page.title.replace(" ", "_")
                    page_found = True
            else:
                print("ERROR: WIKI PAGE DOES NOT EXIST")
        
            count += 1
    return content




'''
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

TOPIC = "Forge FCs matches"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": TOPIC,
    "srlimit": "50"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RANDOMS = DATA["query"]["search"]

for r in RANDOMS:
    print(r["title"])
'''
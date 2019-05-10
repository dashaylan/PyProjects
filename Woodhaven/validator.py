import requests
import links

from bs4 import BeautifulSoup


def query_google():

    req = requests.get("{}".format(links.VANCE))

    soup = BeautifulSoup(req.text, 'html.parser')

    tbl = soup.findAll("tr", {"style": "height:20px;"})

    for thing in tbl:

        rows = thing.findAll(td_and_dir)
        for r in rows:
            print(r)

        print("\n\n")



def td_and_dir(tag):
    return tag.has_attr('class') and tag.has_attr('dir')

query_google()
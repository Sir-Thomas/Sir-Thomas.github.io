from bs4 import BeautifulSoup
from dateutil.parser import parse
from requests_html import HTMLSession

# url = input("Enter patch notes url: ")
url = "https://www.nexon.com/maplestory/news/update/36809/updated-3-20-v-267-maple-story-x-one-punch-man-patch-notes#SunnySunday"

session = HTMLSession()
response = session.get(url)
response.html.render(wait=3, sleep=2, timeout=30)

soup = BeautifulSoup(response.html.html, "html.parser")
table = soup.find_all("table")[-1]
elements = table.find_all("td")

for date_td, event_td in zip(*[iter(elements)] * 2):
    date = parse(date_td.text.replace("Special Sunday", ""))
    date = date.strftime("%Y-%m-%d")
    print(date, end="")
    match event_td.text:
        case "30% reduced chance of item destruction when enhancing items below 21-Stars":
            

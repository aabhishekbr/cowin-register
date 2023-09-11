import requests
from bs4 import BeautifulSoup
pages=4
print("Action , Stock Name ,       Target ,                    Suggested By")
for scrappage in range(1,pages+1):
    url=f"https://www.moneycontrol.com/stocks/advice/display_more.php?pageno={scrappage}&search_flag=view_all&sel_scid=&sel_celeb=&sel_brok="
    #print(url)
    response = requests.get(url)  # Getting page HTML through request
    soup = BeautifulSoup(response.text, 'lxml') # Parsing content using beautifulsoup
    title_paragraphs = soup.find_all('p', class_='title')
    stocklist=[]
    for paragraph in title_paragraphs:
        b=paragraph.text
        #print(b)
        b=b.replace(';',',').replace('Buy','Buy,').replace("Hold","Hold,").replace(":",",")
        stocklist.append(b.strip())

    #print(stocklist)
    for vsl in stocklist:

        print(vsl)


print("-------------------------------Completed scrapping for page no "+str(scrappage))

import requests
from bs4 import BeautifulSoup

url = "https://www.ratemyprofessors.com/search.jsp"
def findRating(aTeacher):
    url = "https://www.ratemyprofessors.com/search.jsp"

    querystring = {"query":"+".join(aTeacher.split(" "))}

    headers = {
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "ab527ab8-1999-4667-83d3-1593fb0e360c,b2ba91a5-a537-427d-858d-3069c0754977",
        'Host': "www.ratemyprofessors.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())
    link = None
    for li in soup.find_all('li',class_= 'listing PROFESSOR'):
        for uni in li.find('span',class_='sub'):
            if uni.split(',')[0] == "Boston University":
                link = li.find('a')
                break
    return link


print(findRating("Perry Donham"))
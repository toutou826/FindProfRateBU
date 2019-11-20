import requests
from bs4 import BeautifulSoup
import collections

url = "http://www.bu.edu/phpbin/course-search/section/"
#Input name of the class, find and return section,teacher and time from catalog.
def getClass(name):
    result = []
    Section = collections.namedtuple('Section',['sectionName','teacher','time'])
    #Get response from the name of the class
    querystring = {"t": name}
    response = requests.request("GET", url, params=querystring)

    soup = BeautifulSoup(response.text, "html.parser")
    classList = soup.find_all("td")
    divided = divide(classList, 8)
    #Append section, teacher and time to result
    for lst in divided:
        if lst[0].get_text()[-1] == "1":
            result.append(Section(name + lst[0].get_text(), lst[2].get_text(), lst[5].get_text()))
    return result

#Divide an array of sub array of size n
def divide(arr, n):
    result = []
    for i in range(0, len(arr), n):
        result.append(arr[i:i + n])
    return result



# print(getClass("cascs330"))
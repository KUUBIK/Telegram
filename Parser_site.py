import bs4
import requests
import re
import time

git = 0
response = requests.get('https://yandex.ru/pogoda/astana?from=serp_title')

responseNew = response.text
dom = bs4.BeautifulSoup(response.text)

def platonus():
    url = 'http://platonus.kazatu.kz/loginsecure'
    s = requests.Session()
    data = {    'language':1,
            'login':'Курбанов_Роберт',
            'password':6066
        }
    resp = s.post(url,data = data)

    resp = s.post('http://platonus.kazatu.kz/student_register')
    print(resp.text)



def parsingSite():

    data = dom.findAll("div", 'fact__temp-wrap') #температура сейчас
    print(data)
    print(type(responseNew))
    data = str(data)
    lookfor = r">[−1.\d,%]+"
    parce = re.findall(lookfor, data)
    parce = str(parce)
    lookfor2 = r"(?!,)[−1.\d,%]+"

    parce = re.findall(lookfor2, parce)
    print(parce)





    return parce

def parsingData():

    data = dom.findAll("div", 'fact__props fact__props_position_middle') #температура сейчас
    print(data)
    data = str(data)
    lookfor = r">[−1.\d,%]+"
    parce = re.findall(lookfor, data)
    print(parce)
    lookfor2 = r"(?!,)[−1.\d,%]+"
    parce = str(parce)
    parce = re.findall(lookfor2, parce)
    print(parce)
    del(parce[2])
    return parce


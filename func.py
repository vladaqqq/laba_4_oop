import requests

def func(category):
    a = requests.get(
        f'https://newsdata.io/api/1/latest?country=ru&category={category}'
        f'&apikey=pub_626325b62e27448152224bc042cd14e9dc5a7').json()
    res = []
    for news in a['results']:
        res.append([news['title'], news['link'], news['description']])
    return res



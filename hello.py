import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.fptpyyx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
movies= soup.select('#old_content > table > tbody > tr')

count=-1
for movie in movies:
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('td.point')
    count +=1
    if a is not None:
        title = a.text
        star = b.text
        doc = {
            'title': title,
            'star': star,
            'rank':count
        }
        db.movies.insert_one(doc)
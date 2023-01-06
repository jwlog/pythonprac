import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs=soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:

    artist = song.select_one('td.info > a.artist.ellipsis')
    rank = song.select_one('td.number')
    title = song.select_one('td.info > a.title.ellipsis')

    title = title.text.strip()
    rank = rank.text[0:2].split('\n')[0]
    artist = artist.text

    print(rank,title,artist)
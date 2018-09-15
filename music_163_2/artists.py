import requests,os
from bs4 import BeautifulSoup

class Artists:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }

    def get_artists(self,url):
        response = requests.get(url,headers = self.headers)
        soup = BeautifulSoup(response.text,features='html.parser')
        body = soup.body
        hot_artists = body.find_all('a',class_ = 'msk')
        artists_list =[]
        for artist in hot_artists:
            artist_msg = [] # 保存歌手信息
            artist_id = artist['href'].replace('/artist?id=', '').strip()
            artist_msg.append(artist_id)
            artist_name = artist['title'].replace('的音乐', '').strip()
            artist_msg.append(artist_name)
            artists_list.append(artist_msg)
        print(artists_list)

if __name__ == '__main__':
    artists = Artists()
    artists.get_artists('http://music.163.com/discover/artist/cat')


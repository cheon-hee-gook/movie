import requests
from bs4 import BeautifulSoup

base_url = "https://movie.naver.com/movie/running/current.nhn"

code = ""

URL = base_url+code

url = requests.get(URL)

soup = BeautifulSoup(url.text, "html.parser")

movie_list = soup.select("body > div.basic > div#container > div#content > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li")

for movie in movie_list:

    title = movie.select_one("dl.lst_dsc > dt.tit > a").get_text()
    code = movie.select_one("dl.lst_dsc > dt.tit > a")['href'][28:]
    print(f'title : {title}', end=" ")
    print(f'code : {code}')


from fake_useragent import UserAgent
from requests import get, exceptions
from bs4 import BeautifulSoup
from sys import argv

def get_data(url, to_update):
    headers = {
        "User-Agent": str(UserAgent.chrome),
    }
    r = get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    film_names = soup.find_all('h2', class_='film-name')
    for film_name in film_names:
        link = film_name.a['href']
        title = film_name.a['title']
        input_string = f'TinyZoneTv Link: https://tinyzonetv.cc{link}\nHDToday Link: https://hdtoday.se{link}\nTitle: {title}\n\n'.encode(encoding='utf-8')
        with open(to_update, 'ba') as f1:
            f1.write(input_string)


def series(page_count):
    print("\n\nTv Shows Updating")
    
    with open('series.txt', 'bw') as f0:
        pass
    
    i = 1
    page = []
    
    while i <= page_count:
        try:
            URL = f'https://tinyzonetv.cc/tv-show?page={i}'
            get_data(URL, 'series.txt')
            page.append(i)
            print(f'On Page: {page.pop()}')
            i+=1
        except exceptions.ConnectionError:
            #print(i)
            i = i

def movies(page_count):
    print("\n\nMovies Updating")

    with open('films.txt', 'bw') as f0:
        pass

    i = 1
    page = []

    while i <= page_count:
        try:
            URL = f'https://hdtoday.se/movie?page={i}'
            get_data(URL, 'films.txt')
            page.append(i)
            print(f'On Page: {page.pop()}')
            i+=1
        except exceptions.ConnectionError:
            #print(i)
            i = i




try:
    what = argv[1].lower()
    if(what == "series"):
        pages = int(input("""
                        Enter page count for series available either on 
                            https://tinyzonetv.cc/tv-show, or
                            https://hdtoday.se/tv-show.
                            Default count is 405.
                        """) or 405)
        series(pages)
    elif(what == "movies"):
        pages = int(input("""
                        Enter page count for movies available either on 
                            https://tinyzonetv.cc/movie, or
                            https://hdtoday.se/movie.
                            Default count is 1261.
                        """) or 1261)
        movies(pages)
    elif(what == "both"):
        pages_series = int(input("""
                        Enter page count for series available either on 
                            https://tinyzonetv.cc/tv-show, or
                            https://hdtoday.se/tv-show.
                            Default count is 405.
                        """) or 405)
        series(pages_series)

        pages_movies = int(input("""
                        Enter page count for movies available either on 
                            https://tinyzonetv.cc/movie, or
                            https://hdtoday.se/movie.
                            Default count is 1261.
                        """) or 1261)
        movies(pages_movies)
    else:
        print("""
            Invalid argument.
            python main.py [argv]
            series: to update series list
            movies: to update movies list
            both: to update both
    """)
    
    print("\n\nUpdated!!!")
        
except Exception:
    print("""
            Invalid argument.
            python main.py [argv]
            series: to update series list
            movies: to update movies list
            both: to update both
    """)

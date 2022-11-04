from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
web_html = response.text
soup = BeautifulSoup(web_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.get_text() for movie in all_movies]
movie_titles = movies[::-1]
print(response.raise_for_status())
print(all_movies)
# with open("movies.txt", mode='w', encoding="utf-8") as file:
#     for movie_title in movie_titles:
#         file.write(f'{movie_title}\n')
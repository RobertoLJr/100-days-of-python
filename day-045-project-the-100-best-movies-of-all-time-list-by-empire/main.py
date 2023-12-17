from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Collect all movie titles from the website's list
movie_tags = soup.find_all(name="h3")
movie_titles = [movie.text for movie in movie_tags][::-1]

# Write all movies in a .txt file
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

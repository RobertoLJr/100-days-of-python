from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os
import requests
import spotipy

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"

# Authenticate Spotify app connection
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

user_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD: ")
user_year = user_date.split("-")[0]

response = requests.get(f"{BILLBOARD_ENDPOINT}/{user_date}")
response.raise_for_status()
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")

# Collect the top 100 song titles on that date into a Python list
songs_spans = soup.select("li ul li h3")
songs_titles = [song.text.strip() for song in songs_spans]

# Create a list of Spotify song URIs for the list of song titles
songs_uris = []
i = 1
for track in songs_titles:
    result = sp.search(q=f"track:{track} year:{user_year}", type="track")
    print(f"{i} - {result}")
    i += 1
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")

# Create a new private Spotify playlist
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{user_date} Billboard 100",
    public=False,
    collaborative=False,
    description=f"Top Billboard 100 tracks from {user_date}"
)

sp.playlist_add_items(
    playlist_id=new_playlist["id"],
    items=songs_uris
)

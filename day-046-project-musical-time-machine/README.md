# Day 46 Project: Musical Time Machine

## Concept

This program makes use of web scrapping to get hold of a list of song titles from the
[Billboard Hot 100](https://www.billboard.com/charts/hot-100/) set. However, it is also capable of filtering the list
according to a date provided by the user, hence returning a list of popular songs around that date. Then, it makes
use of the Spotipy module and Spotify API to create a new private playlist for the user Spotify account containing all the
100 tracks (skipping those that are not found within Spotify).

## Requirements

- Spotify Account.
- A Spotify App set up with Client ID and Secret ID as environment variables.

## Usage

1. Create a new Spotify App in the [Developer Dashboard](https://developer.spotify.com/dashboard/) from Spotify (you can set the Redirect URI as `http://example.com`).
2. Provide the Client ID and Secret ID from the App as environment variables for the program to work.
3. Run the program with `python main.py`.
4. Provide a date in the format `YYYY-MM-DD`.
5. If this is the first time you are running the program, a webpage will open asking for permission connection between Billboard and Spotify. In that case, grant permission. If not, the program will use the `token.txt` file with cached information.
6. Copy the URL in the console for the program to be able to get the user ID for your Spotify account.
7. Verify if the playlist was created with all the songs.

## Resources

### Libraries and modules

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [os module](https://docs.python.org/3/library/os.html)
- [Requests: HTTP for Humans Documentation](https://requests.readthedocs.io/en/latest/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/en/2.22.1/#)

### Miscellanea

- [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)
- [Spotify for Developers](https://developer.spotify.com/)
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from googlesearch import search
import pyautogui
import sys

#RUN MAIN.PY IN CONSOLE USING "python  main.py" THEN RUSH AND CLICK IN YOUR BROWSER WINDOW PLSSSS

# plz replace these with ur own spotify dev values
SPOTIPY_CLIENT_ID = "ur-client-id-here"
SPOTIPY_CLIENT_SECRET = "ur-client-secret-id-here"

# do not change this tho
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

previous_url = None

def get_current_track():
    track_info = sp.current_user_playing_track()
    if track_info and track_info['is_playing']:
        track_name = track_info['item']['name']
        artists = ', '.join(artist['name'] for artist in track_info['item']['artists'])
        return f"{artists} {track_name}"
    return None

def close_previous_tab():
    pyautogui.hotkey('ctrl', 'w')

def search_lyrics(track_query):
    global previous_url
    query = f"genius lyrics {track_query}"
    for url in search(query, num=1):
        if previous_url:
            close_previous_tab()
        webbrowser.open(url)
        previous_url = url
        break

def main():
    last_track = None
    while True:
        current_track = get_current_track()
        if current_track and current_track != last_track:
            print(f"new track loaded : {current_track}")
            search_lyrics(current_track)
            last_track = current_track
        time.sleep(1)

if __name__ == "__main__":
    main()

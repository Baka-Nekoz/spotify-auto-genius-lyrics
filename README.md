# Spotify Auto Genius Lyrics Finder !

A simple python code to load in your currently opened browser window the Genius Lyrics page of the current song playing on your spotify account.


## Setup & Usage

### Step 1

Please start by downloading the repo or the release, then open a command prompt in the project directory on your machine and run `pip install -r requirements.txt`

### Step 2
Open the main.py file in the text/code editor of your choice and replace the following values with your own :
```
SPOTIPY_CLIENT_ID  =  "ur-client-id-here"
SPOTIPY_CLIENT_SECRET  =  "ur-client-secret-id-here"
```

**If you have NO IDEA how to get these FIRST OF ALL what?? Then visit https://developer.spotify.com/dashboard 🙏🙏**

### Step 3
(Before u continue, **make sure you have an active browser window opened somewhere**. This script works with any web browser **AS LONG AS** your browser tab closing shortcut is set as the default **CTRL + W** shortcut)

When done, play any track or queue in spotify and simply run `python main.py` in your previously opened command prompt. Then **RUSH AND CLICK IN YOUR BROWSER WINDOW** because if you don't it will CTRL + W any random window that is currently active lmao) 

### Step 4
Keep the script running in the cmd prompt for as long as you want then close it when you're bored using **CTRL + C**
Enjoy!!!

> **Note:** (ik thats sketchy af im gonna fix this later eventually but since every browser has its own different (if none) API, using **CTRL + W** keystroke was the only workaround i found atm to close the previous lyrics page)

> **Note 2:** also make sure the browser your using to display the lyrics on is also your OS default browser

> **Note 3:** I am **NOT** responsible if my script accidentaly **CTRL + W** your 1800+ lines unsaved CSS opened in your notepad++ window like bro rtfm (and stop using notepad++ istg)

## How does it work ?

read the code its python like come on

no but more seriously tho it gets (every second) the current track playing on your spotify account, searches in your browser for the genius lyrics page, closes the active genius lyrics tab of the previous song if already opened then loads the Genius lyrics page of the currently playing track in a new tab. It also detects when you skip a song, obviously

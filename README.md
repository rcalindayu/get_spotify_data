# get_spotify_data
 Obtain data from the Spotify worldwide ranking chart and tracks and user playlists data using Spotify webAPI

## 0. Setting up your spotify credentials
Follow the instructions at the [Spotify for Developers Quick Start page](https://developer.spotify.com/documentation/web-api/quick-start/) and follow up to the *Set Up Your Account* section. Alternatively, you may follow this [tutorial](https://developer.spotify.com/documentation/general/guides/authorization-guide/)

Make a new app and copy the Client ID and Secret Code.

## 1. scrape_spotify_charts.py
Based from automated data collection from Spotify's worldwide ranking in 50+ countries from [edumucelli](https://github.com/edumucelli/spotify-worldwide-ranking). A snapshot of the data collected by the code has been published at [Kaggle datasets](https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking).

On the command line, run by:
````
python scrape_spotify_charts.py
````
or alternatively, in the jupyter notebook
````
%run scrape_spotify_charts.py
````
Specify the desired region, start and end date, and directory.

## 2. consolidate_spotify_daily_charts.ipynb
Use this notebook to consolidate the daily charts data into monthly and a single unified file

## 3. set_credentials.ipynb

Install the [`keyring`](https://keyring.readthedocs.io/en/latest/) package
````
pip install keyring 
````
The Python keyring library provides an easy way to access the system keyring service from python. It can be used in any application that needs safe password storage. 

Run the notebook. Keyring will ask for your Spotify Client ID and Secret Code and safely hold it in your device.

For the notebooks below, please also install the [`spotipy`](https://spotipy.readthedocs.io/en/2.12.0/) python module 
````
pip install spotipy
````
## 4.  get_spotify_track_artist_data.ipynb
Use this notebook to get Spotify track data for the tracks ranking in the daily charts data

## 5. get_spotify_playlists.ipynb
Use this notebook to get spotify playlists based on a spotipy query object 



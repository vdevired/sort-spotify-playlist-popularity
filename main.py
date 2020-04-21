import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CID = #YOUR CLIENT_ID
SECRET = #YOUR CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = input("What playlist? ")
playlist = sp.playlist_tracks(playlist_id=playlist_id)

artist_names = []
track_names = []
popularitys = []

for t in playlist["items"]:
    t = t["track"]  
    artist_names.append(t["artists"][0]["name"])
    track_names.append(t["name"])
    popularitys.append(t["popularity"])

playlist_dataframe = pd.DataFrame({'artist_name' : artist_names, 'track_name' : track_names, 'popularity' : popularitys})
playlist_dataframe.sort_values(by=["popularity"], ascending=False, inplace=True)
print(playlist_dataframe.to_string())
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify app credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3edd9c68f0b14e69a9c498d71f2d5f67",
                                               client_secret="da016bdfbd124506bd57f799478df068",
                                               redirect_uri="skeepertech.netlify.app",
                                               scope="playlist-read-private"))

# Replace 'spotify_playlist_uri' with your playlist URI
playlist_uri = 'spotify:playlist:https://open.spotify.com/playlist/5qNM7VrKsD1nuuslk6QunG?si=37c7651ccc144b39'

# Fetch the playlist
playlist = sp.playlist(playlist_uri)

# Print the playlist's name and total tracks
print(f"Playlist: {playlist['name']}")
print(f"Total tracks: {playlist['tracks']['total']}")

# Loop through each track and print its name and artists
for track in playlist['tracks']['items']:
    track_name = track['track']['name']
    track_artists = ', '.join([artist['name'] for artist in track['track']['artists']])
    print(f"{track_name} by {track_artists}")

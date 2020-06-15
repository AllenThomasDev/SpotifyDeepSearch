# SpotifyDeepSearch
Add-on created on top of Spotipy to search similar artists. Recursive depth and width can also be specified to give a larger network of artists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install **Spotipy** package for Python which can be found **[here](https://spotipy.readthedocs.io/en/2.12.0/#installation)** to make use of Spotify's API. Future builds will remove this dependency on Spotipy.

You will also need **Pandas** as artist data are stored in pandas.DataFrames and are then saved as .csv files.

### Installing
```
pip install spotipy
pip install pandas
```
You could also use-
```python
pip install -r requirements.txt
```
### What it does-

Spotify's API provides an [endpoint](https://developer.spotify.com/documentation/web-api/reference/artists/get-related-artists/) which returns a collection of upto 20 artists similar to a given artist.

DeepSearch recursively searches for related artists according to the given depth and width.
addEdge() takes 3 parameters-
```python
addedge(artist_id,depth,width):
```
artist_id - The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist.

depth - The number of related artists can be limited by passing a depth value. The maximum value is the default value - 20.

width - This is the recursive height of the search.

### Examples


## Authors

* **Allen Thomas** - [AllenThomasDev](https://github.com/AllenThomasDev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



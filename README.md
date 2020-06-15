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

addEdge(,20,0) will return 2 dataframes. One with the 'connections' and one with the details for every artist.

|----|-------------|--------------------|
|  0 | Frank Ocean | Tyler, The Creator |
|  1 | Frank Ocean | Earl Sweatshirt    |
|  2 | Frank Ocean | Kevin Abstract     |
|  3 | Frank Ocean | BROCKHAMPTON       |
|  4 | Frank Ocean | SZA                |
|  5 | Frank Ocean | The Internet       |
|  6 | Frank Ocean | Chance the Rapper  |
|  7 | Frank Ocean | Kanye West         |
|  8 | Frank Ocean | Brent Faiyaz       |
|  9 | Frank Ocean | Solange            |
| 10 | Frank Ocean | Syd                |
| 11 | Frank Ocean | Childish Gambino   |
| 12 | Frank Ocean | Sampha             |
| 13 | Frank Ocean | Odd Future         |
| 14 | Frank Ocean | Jhené Aiko         |
| 15 | Frank Ocean | Majid Jordan       |
| 16 | Frank Ocean | Daniel Caesar      |
| 17 | Frank Ocean | KIDS SEE GHOSTS    |
| 18 | Frank Ocean | dvsn               |
| 19 | Frank Ocean | Kali Uchis         |



## Authors

* **Allen Thomas** - [AllenThomasDev](https://github.com/AllenThomasDev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



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

connections -

|    | source      | target             |
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

|    | name               |   followers | genres                                                                                                                                                            |   popularity | uri                                   |
|----|--------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------|
|  0 | Solange            |     1076339 | ['afrofuturism', 'alternative r&b', 'art pop', 'dance pop', 'electropop', 'escape room', 'hip pop', 'indie soul', 'neo soul', 'pop', 'r&b', 'urban contemporary'] |           69 | spotify:artist:2auiVi8sUZo17dLy1HwrTU |
|  1 | Earl Sweatshirt    |     1194533 | ['alternative hip hop', 'escape room', 'experimental hip hop', 'hip hop', 'rap', 'underground hip hop']                                                           |           71 | spotify:artist:3A5tHz1SfngyOZM2gItYKu |
|  2 | Tyler, The Creator |     4458285 | ['hip hop', 'rap']                                                                                                                                                |           86 | spotify:artist:4V8LLVI7PbaPR0K2TGSxFF |
|  3 | Chance the Rapper  |     4834102 | ['chicago rap', 'conscious hip hop', 'hip hop', 'pop rap', 'rap']                                                                                                 |           84 | spotify:artist:1anyVhU62p31KFi8MEzkbf |
|  4 | BROCKHAMPTON       |     1440198 | ['boy band', 'hip hop', 'pop', 'rap']                                                                                                                             |           81 | spotify:artist:1Bl6wpkWCQ4KVgnASpvzzA |
|  5 | Kevin Abstract     |      449848 | ['hip hop', 'lgbtq+ hip hop', 'rap']                                                                                                                              |           68 | spotify:artist:07EcmJpfAday8xGkslfanE |
|  6 | The Internet       |      790823 | ['alternative r&b', 'escape room', 'indie soul', 'lgbtq+ hip hop']                                                                                                |           66 | spotify:artist:7GN9PivdemQRKjDt4z5Zv8 |
|  7 | Frank Ocean        |     5808144 | ['alternative r&b', 'hip hop', 'lgbtq+ hip hop', 'neo soul', 'pop']                                                                                               |           86 | spotify:artist:2h93pZq0e7k5yf4dywlkpM |
|  8 | SZA                |     3347854 | ['pop', 'pop rap', 'rap']                                                                                                                                         |           83 | spotify:artist:7tYKF4w9nC0nq9CsPZTHyP |
|  9 | Brent Faiyaz       |      683784 | ['alternative r&b', 'dmv rap', 'rap']                                                                                                                             |           78 | spotify:artist:3tlXnStJ1fFhdScmQeLpuG |
| 10 | Kanye West         |    11754205 | ['chicago rap', 'rap']                                                                                                                                            |           91 | spotify:artist:5K4W6rqBFWDnAN6FQUkS6x |

## Authors

* **Allen Thomas** - [AllenThomasDev](https://github.com/AllenThomasDev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



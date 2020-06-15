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

| index | Source | Target |
| --- | --- | --- |
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

edges-
|    | name               |   followers | genres                                                                                                                                                            |   popularity | uri                                   |
|----|--------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------|
|  0 | SZA                |     3345108 | ['pop', 'pop rap', 'rap']                                                                                                                                         |           83 | spotify:artist:7tYKF4w9nC0nq9CsPZTHyP |
|  1 | Frank Ocean        |     5803107 | ['alternative r&b', 'hip hop', 'lgbtq+ hip hop', 'neo soul', 'pop']                                                                                               |           86 | spotify:artist:2h93pZq0e7k5yf4dywlkpM |
|  2 | Chance the Rapper  |     4832323 | ['chicago rap', 'conscious hip hop', 'hip hop', 'pop rap', 'rap']                                                                                                 |           84 | spotify:artist:1anyVhU62p31KFi8MEzkbf |
|  3 | KIDS SEE GHOSTS    |      526794 | ['hip hop', 'rap', 'underground hip hop']                                                                                                                         |           68 | spotify:artist:2hPgGN4uhvXAxiXQBIXOmE |
|  4 | Daniel Caesar      |     1972912 | ['canadian contemporary r&b', 'pop']                                                                                                                              |           80 | spotify:artist:20wkVLutqVOYrc0kxFs7rA |
|  5 | Odd Future         |      673015 | ['hip hop', 'rap']                                                                                                                                                |           56 | spotify:artist:5xpkLC1MxiPRiIJUDEzuVm |
|  6 | BROCKHAMPTON       |     1438742 | ['boy band', 'hip hop', 'pop', 'rap']                                                                                                                             |           81 | spotify:artist:1Bl6wpkWCQ4KVgnASpvzzA |
|  7 | Brent Faiyaz       |      682256 | ['alternative r&b', 'dmv rap', 'rap']                                                                                                                             |           78 | spotify:artist:3tlXnStJ1fFhdScmQeLpuG |
|  8 | dvsn               |      760351 | ['alternative r&b', 'canadian contemporary r&b', 'deep pop r&b', 'pop', 'r&b', 'trap soul', 'urban contemporary']                                                 |           72 | spotify:artist:7e1ICztHM2Sc4JNLxeMXYl |
|  9 | Earl Sweatshirt    |     1193800 | ['alternative hip hop', 'escape room', 'experimental hip hop', 'hip hop', 'rap', 'underground hip hop']                                                           |           71 | spotify:artist:3A5tHz1SfngyOZM2gItYKu |
| 10 | Sampha             |      422793 | ['alternative r&b', 'indie r&b', 'indie soul']                                                                                                                    |           65 | spotify:artist:2WoVwexZuODvclzULjPQtm |
| 11 | Tyler, The Creator |     4452752 | ['hip hop', 'rap']                                                                                                                                                |           86 | spotify:artist:4V8LLVI7PbaPR0K2TGSxFF |
| 12 | Solange            |     1075381 | ['afrofuturism', 'alternative r&b', 'art pop', 'dance pop', 'electropop', 'escape room', 'hip pop', 'indie soul', 'neo soul', 'pop', 'r&b', 'urban contemporary'] |           69 | spotify:artist:2auiVi8sUZo17dLy1HwrTU |
| 13 | Jhené Aiko         |     3243980 | ['alternative r&b', 'pop', 'r&b', 'urban contemporary']                                                                                                           |           84 | spotify:artist:5ZS223C6JyBfXasXxrRqOk |
| 14 | Kevin Abstract     |      449341 | ['hip hop', 'lgbtq+ hip hop', 'rap']                                                                                                                              |           68 | spotify:artist:07EcmJpfAday8xGkslfanE |
| 15 | Kanye West         |    11748468 | ['chicago rap', 'rap']                                                                                                                                            |           91 | spotify:artist:5K4W6rqBFWDnAN6FQUkS6x |
| 16 | Majid Jordan       |      504182 | ['alternative r&b', 'pop', 'trap soul']                                                                                                                           |           70 | spotify:artist:4HzKw8XcD0piJmDrrPRCYk |
| 17 | Childish Gambino   |     6375090 | ['atl hip hop', 'hip hop', 'pop rap', 'rap']                                                                                                                      |           84 | spotify:artist:73sIBHcqh3Z3NyqHKZ7FOL |
| 18 | The Internet       |      790311 | ['alternative r&b', 'escape room', 'indie soul', 'lgbtq+ hip hop']                                                                                                |           66 | spotify:artist:7GN9PivdemQRKjDt4z5Zv8 |
| 19 | Kali Uchis         |      954914 | ['art pop', 'colombian pop', 'pop']                                                                                                                               |           79 | spotify:artist:1U1el3k54VvEUzo3ybLPlM |
| 20 | Syd                |      311888 | ['alternative r&b', 'escape room', 'indie r&b', 'lgbtq+ hip hop']                                                                                                 |           68 | spotify:artist:3jk39CGeaaSO3FPKNx1RUx |


## Authors

* **Allen Thomas** - [AllenThomasDev](https://github.com/AllenThomasDev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



<p>
  <h1>SpotifyDeepSearch  <img src="https://developer.spotify.com/assets/branding-guidelines/icon1@2x.png" width="50" title="hover text"></h1>
 
</p>
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

eg. 
```python
addEdge(https://open.spotify.com/artist/2h93pZq0e7k5yf4dywlkpM,10,0)
```
depth = 10, so the number of related artists will be limited to 10. And because width is set to 0, additional searches will not take place for every related artist -

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


```python
addEdge(https://open.spotify.com/artist/2h93pZq0e7k5yf4dywlkpM,3,2)
```
depth = 3, so the number of related artists will be limited to 3.This time the width is set to 2, so related artists will be searched to levels.
The difference in output will make things clearer-
|    | source             | target             |
|----|--------------------|--------------------|
|  0 | Frank Ocean        | Tyler, The Creator |
|  1 | Frank Ocean        | Earl Sweatshirt    |
|  2 | Frank Ocean        | Kevin Abstract     |
|  3 | Tyler, The Creator | Earl Sweatshirt    |
|  4 | Tyler, The Creator | Domo Genesis       |
|  5 | Tyler, The Creator | KIDS SEE GHOSTS    |
|  6 | Earl Sweatshirt    | MellowHype         |
|  7 | Earl Sweatshirt    | Domo Genesis       |
|  8 | Earl Sweatshirt    | Vince Staples      |
|  9 | Domo Genesis       | Mike G             |
| 10 | Domo Genesis       | MellowHype         |
| 11 | Domo Genesis       | MellowHigh         |
| 12 | KIDS SEE GHOSTS    | JPEGMAFIA          |
| 13 | KIDS SEE GHOSTS    | Ameer Vann         |
| 14 | KIDS SEE GHOSTS    | Kevin Abstract     |
| 15 | Kevin Abstract     | BROCKHAMPTON       |
| 16 | Kevin Abstract     | Matt Champion      |
| 17 | Kevin Abstract     | Ameer Vann         |
| 18 | BROCKHAMPTON       | Kevin Abstract     |
| 19 | BROCKHAMPTON       | Matt Champion      |
| 20 | BROCKHAMPTON       | JPEGMAFIA          |
| 21 | Matt Champion      | Ameer Vann         |
| 22 | Matt Champion      | Yeek               |
| 23 | Matt Champion      | Duckwrth           |
| 24 | Ameer Vann         | Matt Champion      |
| 25 | Ameer Vann         | Tabby              |
| 26 | Ameer Vann         | Duckwrth           |

|    | name               |   followers | genres                                                                                                                        |   popularity | uri                                   |
|----|--------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------|
|  0 | BROCKHAMPTON       |     1440198 | ['boy band', 'hip hop', 'pop', 'rap']                                                                                         |           81 | spotify:artist:1Bl6wpkWCQ4KVgnASpvzzA |
|  1 | Domo Genesis       |      203264 | ['alternative hip hop', 'hip hop', 'rap', 'underground hip hop']                                                              |           59 | spotify:artist:6vHBuUxrcpn1do5UaEJ7g6 |
|  2 | Duckwrth           |      164485 | ['alternative r&b', 'escape room', 'underground hip hop']                                                                     |           68 | spotify:artist:6I3MElirhT5t6Kf7p0hGk9 |
|  3 | Earl Sweatshirt    |     1194533 | ['alternative hip hop', 'escape room', 'experimental hip hop', 'hip hop', 'rap', 'underground hip hop']                       |           71 | spotify:artist:3A5tHz1SfngyOZM2gItYKu |
|  4 | Mike G             |       57220 | []                                                                                                                            |           45 | spotify:artist:1QdjL34EAib5zndNoqA2ly |
|  5 | Yeek               |      116227 | ['alternative r&b', 'indie r&b']                                                                                              |           63 | spotify:artist:5BhFZpE8kUGZJiKOsYjLQM |
|  6 | Matt Champion      |      116726 | ['bedroom pop']                                                                                                               |           57 | spotify:artist:29Oq9Nv8zLgu3IvX1tIpbm |
|  7 | Tabby              |       16632 | ['minnesota hip hop']                                                                                                         |           40 | spotify:artist:2Yp114orhinD5W0DioIKER |
|  8 | MellowHype         |      145002 | ['hip hop', 'underground hip hop']                                                                                            |           44 | spotify:artist:5CCrgHVEWtg8YTEn1UaYug |
|  9 | KIDS SEE GHOSTS    |      527520 | ['hip hop', 'rap', 'underground hip hop']                                                                                     |           68 | spotify:artist:2hPgGN4uhvXAxiXQBIXOmE |
| 10 | MellowHigh         |       53157 | ['underground hip hop']                                                                                                       |           34 | spotify:artist:0B1prtAE9Ca9hTs0rUkjHG |
| 11 | JPEGMAFIA          |      233786 | ['alternative hip hop', 'escape room', 'experimental hip hop', 'hip hop', 'industrial hip hop', 'rap', 'underground hip hop'] |           67 | spotify:artist:6yJ6QQ3Y5l0s0tn7b0arrO |
| 12 | Ameer Vann         |       74062 | ['hip hop', 'underground hip hop']                                                                                            |           52 | spotify:artist:7kIbB1pdDyehFj8aNgfzfH |
| 13 | Kevin Abstract     |      449848 | ['hip hop', 'lgbtq+ hip hop', 'rap']                                                                                          |           68 | spotify:artist:07EcmJpfAday8xGkslfanE |
| 14 | Tyler, The Creator |     4458285 | ['hip hop', 'rap']                                                                                                            |           86 | spotify:artist:4V8LLVI7PbaPR0K2TGSxFF |
| 15 | Vince Staples      |     1105510 | ['conscious hip hop', 'escape room', 'hip hop', 'rap', 'southern hip hop', 'underground hip hop']                             |           73 | spotify:artist:68kEuyFKyqrdQQLLsmiatm |
| 16 | Frank Ocean        |     5808144 | ['alternative r&b', 'hip hop', 'lgbtq+ hip hop', 'neo soul', 'pop']                                                           |           86 | spotify:artist:2h93pZq0e7k5yf4dywlkpM |


## Authors

* **Allen Thomas** - [AllenThomasDev](https://github.com/AllenThomasDev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



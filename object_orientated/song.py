#What is the most interesting part of this.
#You can create more than 2 classes in a file.

class Song():
    """Classes to represent song
    Attributes:
        title(str): The title of the song.
        artist(artist): An artist object representing
        durtation(int): THe duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title(str): Intialises the 'title' attribute.
            artist(Artist): At artist object representing the song's creator
            duration(Optional[int]: Initial value for the duration attribute.
            default to value if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album():
    """Class to represent to An Album, ysing it's track list
    Attributes:
        album_name(str): The name of the album
        year (int): The year the album was released.
        artist (Artist):  Responsible for creating the song,
                        If not specified, default is "Various Artists"
        tracks(list)[song]: A list of the song on the album

    Methods:
        add_song: Used to add a new song to the album track list.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.artist = artist
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = [] #List

    def add_song(self, song, position=None):
        """Adds a song to the track list
        Args:
            song (Song): A song to add
            position (Optional)[int]: If specified the song will be added tho that position in the track list.

                """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attriabutes:
    name(str) : THe name of the artist.
    albums(list(album): A list of the albums by this artist.
                        The list includes only those albums in this collection, it is
                        not an exhaustive list of the artists's published albums.
    Methods:
        add_album: Use to add a new album tho the aritsts albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new alum to the list

        Args:
             album(Album): Album object to add to the list.
                If  the album is already present, it will not be added again (Although this is yet to be implelemented)
            """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row has consist of (artist, album, year song):
            artist_field, artist_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
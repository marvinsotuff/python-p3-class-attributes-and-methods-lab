class Song:
    # ---------- CLASS ATTRIBUTES ----------
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # update counters and lists when a new song is created
        type(self).add_song_to_count()
        type(self).add_to_artists(artist)
        type(self).add_to_genres(genre)
        type(self).add_to_artist_count(artist)
        type(self).add_to_genre_count(genre)

    # ---------- CLASS METHODS ----------
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


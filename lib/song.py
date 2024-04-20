class Song:

    count = 0 

    genres = []

    genre_count = {}

    artists = []

    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_count()
        self.add_genre(genre)
        self.add_artist(artist)
        

    @classmethod
    def add_count(cls):
        cls.count += 1 

    @classmethod
    def add_genre(cls, genre):
        if cls.genres.__contains__(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genres.append(genre)
            cls.genre_count.update({genre: 1})

    @classmethod
    def add_artist(cls, artist):
        if cls.artists.__contains__(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artists.append(artist)
            cls.artist_count.update({artist: 1})

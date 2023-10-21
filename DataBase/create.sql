CREATE TABLE Collection (
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	year_of_release DATE
);

CREATE TABLE Albums (
	album_id INTEGER PRIMARY KEY,
	title VARCHAR(100),
	year_of_release DATE
);

CREATE TABLE Song (
	song_id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	duration INT,
	album_id INTEGER REFERENCES Albums(album_id)
);

CREATE TABLE Song_collection(
	song_id INTEGER REFERENCES Song(song_id),
	collection_id INTEGER REFERENCES Collection(song_id),
	CONSTRAINT pk PRIMARY KEY (song_id, collection_id)
);

CREATE TABLE Artist (
	artist_id SERIAL PRIMARY KEY,
	nickname VARCHAR(50)
);

CREATE TABLE Genres (
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE Genre_Artist (
	artist_id INTEGER REFERENCES Artist(artist_id),
	genre_id INTEGER REFERENCES Genres(genre_id),
	CONSTRAINT pk PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE Album_author (
	album_id INTEGER REFERENCES Albums (album_id),
	artist_id INTEGER REFERENCES Artist (artist_id),
	CONSTRAINT pk PRIMARY KEY (album_id, artist_id)
);

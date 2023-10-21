--Количество исполнителей в каждом жанре.
SELECT Genres.name AS "Жанр", COUNT(Genre_Artist.artist_id) AS "Количество исполнителей"
FROM Genres
LEFT JOIN Genre_Artist ON Genres.genre_id = Genre_Artist.genre_id
GROUP BY Genres.name;

--Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(Song.song_id) AS "Количество треков"
FROM Song
INNER JOIN Albums ON Song.album_id = Albums.album_id
WHERE Albums.year_of_release BETWEEN '2019-01-01' AND '2020-12-31';

--Средняя продолжительность треков по каждому альбому.
SELECT Albums.title AS "Название альбома", AVG(Song.duration) AS "Средняя продолжительность (секунд)"
FROM Albums
INNER JOIN Song ON Albums.album_id = Song.album_id
GROUP BY Albums.title;

--Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT DISTINCT Artist.artist_name AS "Имя исполнителя"
FROM Artist
LEFT JOIN Album_author ON Artist.artist_id = Album_author.artist_id
LEFT JOIN Albums ON Album_author.album_id = Albums.album_id
WHERE Albums.year_of_release IS NULL OR Albums.year_of_release != '2020-01-01';

-- Названия сборников, в которых присутствует конкретный исполнитель Stray Kids
SELECT Collection.name AS "Название сборника"
FROM Collection
INNER JOIN Song_collection ON Collection.collection_id = Song_collection.collection_id
INNER JOIN Song ON Song_collection.song_id = Song.song_id
INNER JOIN Album_author ON Song.album_id = Album_author.album_id
INNER JOIN Artist ON Album_author.artist_id = Artist.artist_id
WHERE Artist.artist_name = 'Stray Kids'; 


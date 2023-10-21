-- Название и продолжительность самого длительного трека.
SELECT title AS "Трек", duration AS "Продолжительность (в секундах)"
FROM Song
ORDER BY duration DESC
LIMIT 1;

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT title AS "Трек", duration AS "Продолжительность (в секундах)"
FROM Song
WHERE duration >= 210;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name AS "Сборник"
FROM Collection
WHERE year_of_release BETWEEN '2018-01-01' AND '2020-12-31';

--Исполнители, чьё имя состоит из одного слова.
SELECT artist_name AS "Артист"
FROM Artist
WHERE artist_name NOT LIKE '% %';

--Название треков, которые содержат слово «мой» или «my».
SELECT title AS "Трек"
FROM Song
WHERE title ILIKE '%мой%' OR title ILIKE '%my%'; 

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


-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT DISTINCT Albums.title AS "Название альбома"
FROM Albums
INNER JOIN Album_author ON Albums.album_id = Album_author.album_id
INNER JOIN (
    SELECT Album_author.artist_id
    FROM Album_author
    GROUP BY Album_author.album_id, Album_author.artist_id
    HAVING COUNT(DISTINCT Album_author.artist_id) > 1
) multi_genre_artists ON Album_author.artist_id = multi_genre_artists.artist_id;

--Наименования треков, которые не входят в сборники.
SELECT Song.title AS "Наименование трека"
FROM Song
LEFT JOIN Song_collection ON Song.song_id = Song_collection.song_id
WHERE Song_collection.song_id IS NULL;

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT DISTINCT Artist.artist_name AS "Имя исполнителя", Song.title AS "Наименование трека", Song.duration AS "Продолжительность (секунд)"
FROM Artist
INNER JOIN Album_author ON Artist.artist_id = Album_author.artist_id
INNER JOIN Song ON Album_author.album_id = Song.album_id
WHERE Song.duration = (
    SELECT MIN(Song.duration)
    FROM Song
);

-- Названия альбомов, содержащих наименьшее количество треков.
SELECT Albums.title AS "Название альбома", COUNT(Song.song_id) AS "Количество треков"
FROM Albums
LEFT JOIN Song ON Albums.album_id = Song.album_id
GROUP BY Albums.title
HAVING COUNT(Song.song_id) = (
    SELECT MIN(track_count)
    FROM (
        SELECT COUNT(Song.song_id) AS track_count
        FROM Albums
        LEFT JOIN Song ON Albums.album_id = Song.album_id
        GROUP BY Albums.album_id
    ) AS track_counts
);

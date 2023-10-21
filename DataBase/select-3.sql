
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


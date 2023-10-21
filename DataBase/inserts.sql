INSERT INTO Artist (nickname)
VALUES
    ('BTS'),
    ('Stray Kids'),
    ('Le sserafim'),
    ('Dreamcatcher');

INSERT INTO Genres (name)
VALUES
    ('Pop'),
    ('Electropop'),
    ('Hip-Hop');

INSERT INTO Albums (title, year_of_release)
VALUES
    ('Easy', '2020-05-25'),
    ('Forever young', '2018-02-01'),
    ('Dark Side', '2021-03-18');
    ('Fear not', '2022-03-18');

INSERT INTO Song (title, duration, album_id)
VALUES
    ('Domino', 240, 1),
    ('Cry', 180, 1),
    ('Fire', 210, 2),
    ('My universe', 190, 2),
    ('Vision', 220, 3),
    ('Boca', 200, 3);
    ('Unforgiven', 220, 3),
    ('Fearless', 200, 3);
    ('AntiFragile', 235, 3);

INSERT INTO Collection (name, year_of_release)
VALUES
    ('3rd Generation', '2020-12-01'),
    ('4th Generation', '2023-04-05'),
    ('Korean bop', '2021-10-01'),
    ('Hits', '2022-09-01');

INSERT INTO Song_collection (song_id, collection_id)
VALUES
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 1),
    (5, 1),
    (5, 4),
    (6, 1),
    (6, 3),
    (7, 2),
    (7, 3),
    (8, 2);

INSERT INTO Genre_Artist (artist_id, genre_id)
VALUES
    (1, 1),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2);

INSERT INTO Album_author (album_id, artist_id)
VALUES
    (1, 2),
    (2, 1),
    (3, 4),
    (4, 3);


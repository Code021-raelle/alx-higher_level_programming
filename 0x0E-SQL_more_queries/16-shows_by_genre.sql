-- This script lists all shows and their linked genres from the 'hbtn_0d_tvshows' database,
-- including shows without genres, displaying the title of each show and the associated genre
-- name if available, sorted in ascending order by the show title and genre name.

SELECT tv_shows.title, COALESCE((SELECT GROUP_CONCAT(tv_genres.name SEPARATOR ', ') FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.show_id = tv_shows.id), 'NULL') AS name
FROM tv_shows
ORDER BY tv_shows.title ASC, name ASC;

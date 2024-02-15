-- This script lists all TV shows from the 'hbtn_0d_tvshows' database, including those without genres,
-- displaying the title of each show and the associated genre ID if available,
-- sorted in ascending order by both 'tv_shows.title' and 'tv_show_genres.genre_id'.

SELECT tv_shows.title, COALESCE((SELECT tv_show_genres.genre_id FROM tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id ORDER BY tv_show_genres.genre_id LIMIT  1), NULL) AS genre_id
FROM tv_shows
ORDER BY tv_shows.title ASC, genre_id ASC;

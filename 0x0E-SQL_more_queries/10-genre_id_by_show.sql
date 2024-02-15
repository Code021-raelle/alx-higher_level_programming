-- This script lists all TV shows from the 'hbtn_0d_tvshows' database that have at least
-- one genre linked, displaying the title of each show and the associated genre ID,
-- sorted in ascending order by both 'tv_shows.title' and 'tv_show_genres.genre_id'.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
WHERE EXISTS (SELECT   1 FROM tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

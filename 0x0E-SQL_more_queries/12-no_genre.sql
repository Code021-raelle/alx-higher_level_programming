-- This script lists all TV shows from the 'hbtn_0d_tvshows' database that do not have
-- any genres linked, displaying the title of each show and NULL for the genre ID,
-- sorted in ascending order by 'tv_shows.title'.

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE NOT EXISTS (SELECT   1 FROM tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id)
ORDER BY tv_shows.title ASC;

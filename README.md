
## Introduction

Movie Trailer Website is my first project with Udacity on their Full Stack Web Developer Nanodegree course. It focuses on writing server side code to display movies in an HTML format so that users can watch trailers and find out other information on a list of movies.


## Requirements

* python >= 2.7
* web browser: any recent stable release of Safari/Chrome/Firefox


## Usage

Run `entertainment_center.py`:

* `python <path>/entertainment_center.py`
* To add more movies, add more movies to the `movies` list in `entertainment_system.py`.

## Details

* `entertainment_center.py` module creates a list of movies.
* It passes this list to `open_movies_page()` function in `fresh_tomatoes.py`.
* `open_movies_page()` generates a static web page with the movie title, poster images, youtube URL, Rating, and storyline for each movie in the list.
* The `Movie` class defined in `media.py` module and is a child of `Video`. The `Video` class stores basic information such as `title` and `duration` that can be extended by `Movie` and any other classes that may be added in the future, such as `TvShow` to store information on TV Shows. The `Movie` class stores `storyline`, `poster_image_url`, `trailer_youtube_url`, and `rating` for a particular movie.
*  A Use can click on movie poster image to see it's youtube trailer.
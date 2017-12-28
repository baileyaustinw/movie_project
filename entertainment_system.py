import fresh_tomatoes
import media

star_wars = media.Movie("Star Wars: The Last Jedi",
					125,
					"Luke Skywalker's peaceful and solitary existence gets "
					"upended when he encounters Rey, a young woman who shows"
					" strong signs of the Force.",
					"http://t2.gstatic.com/images?q=tbn:ANd9GcRgcIU4MKHZkZNeDt_"
					"tAewyfwX7PAmSdj_7wdg_FInkZw8Um9F_",
					"https://www.youtube.com/watch?v=Q0CbN8sfihY",
					"PG-13")
thor = media.Movie("Thor: Ragnarok",
					130,
					"Thor's quest for survival leads him in a race against time"
					"to prevent the all-powerful Hela from destroying his home "
					"world and the Asgardian civilization.",
					"http://t3.gstatic.com/images?q=tbn:ANd9GcST1uigGrukMvSAVUe"
					"fFNuQ0NMZAR-FjfFIwSZFCR5ZkyMSgCyj",
					"https://www.youtube.com/watch?v=ue80QwXMRHg",
					"PG-13")
justice_league = media.Movie("Justice League",
							120,
							"Together, Batman and Wonder Woman work quickly to "
							"recruit a team to stand against this newly awakened"
							" enemy.",
							"http://t0.gstatic.com/images?q=tbn:ANd9GcTbr9aajZt"
							"JiuhXc_biRws9jzCi4u1q4MWvyPVe0rGO9Z0RwDqT",
							"https://www.youtube.com/watch?v=r9-DM9uBtVI",
							"PG-13")
bright = media.Movie("Bright",
					117,
					"Battling both their own personal differences as well as an"
					"onslaught of enemies, they must work together to protect "
					"a young female elf and a thought-to-be-forgotten relic, "
					"which, in the wrong hands, could destroy everything.",
					"http://t3.gstatic.com/images?q=tbn:ANd9GcRUPw1tUlZetUPe3Yi"
					"CSeQwYqp3LuvnVO7EdgByGdBXITfFR-9Y",
					"https://www.youtube.com/watch?v=6EZCBSsBxko",
					"R")

avatar = media.Movie("Avatar",
					162,
					"On the lush alien world of Pandora live the Na'vi, beings"
					" who appear primitive but are highly evolved.",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teas"
					"er-Poster.jpg",
					"https://www.youtube.com/watch?v=d1_JBMrrYw8",
					"PG-13")
school_of_rock = media.Movie("School of Rock",
							109,
							"Overly enthusiastic guitarist Dewey Finn (Jack "
							"Black) gets thrown out of his bar band and finds"
							" himself in desperate need of work.",
							"http://www.gstatic.com/tv/thumb/movieposters/33094"
							"/p33094_p_v8_aa.jpg",
							"https://www.youtube.com/watch?v=3PsUJFEBC74",
							"PG-13")

movies = [star_wars, thor, justice_league, bright, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
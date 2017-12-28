import webbrowser

class Video():
	""" This class serves as a parent class for Movie """
	def __init__(self, title, duration):
		self.title = title
		# duration is set in minutes
		self.duration = duration

class Movie(Video):
	""" This class provides a way to store movie related information """
	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

	def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube, rating):
		Video.__init__(self, title, duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		if rating in self.VALID_RATINGS:
			self.rating = rating
		else:
			self.rating = None

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

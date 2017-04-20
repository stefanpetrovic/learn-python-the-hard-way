class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics;

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday_song = Song(["Happy birthday to you", "I 'don't want to get sued"])

happy_bday_song.sing_me_a_song()
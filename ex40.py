class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
birthdaySong = "Happy birthday to you\nI don't want to be sued\nSo I'll stop right there"
happy_bday = Song([birthdaySong])

bullSong = "They rally around the family\nWith pockets full of shells"
bulls_on_parade = Song([bullSong])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

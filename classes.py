class Jukebox:
    def __init__(self):
        self.name = "jukebox"
        self.song_list = ['Song1']
        
    def play(self, num):
        print('playing {0}'.format(self.song_list[num - 1]))


jukebox = Jukebox()

jukebox.song_list.append('Song2')

user_input = input('Enter p to play: ')
user_num = input('Which song: ')

if user_input == 'p':
    jukebox.play(int(user_num))
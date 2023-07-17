class Song:

    def __init__(self, track, artists, duration):
        self.track = track
        self.artists = artists
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.track)
        print(self.artists)
        print(self.duration)
        print("CURRENT:", self, "NEXT:", self.next, "PREVIOUS:", self.previous)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, song):
        self.size += 1

        if self.head is None:
            self.head = song
            self.tail = song
        else:
            self.tail.next = song
            song.previous = self.tail

            # Any newly added song will be tail :)
            self.tail = song

            # CIRCULAR
            self.tail.next = self.head
            self.head.previous = self.tail

    def iterate(self, direction=0):
        if direction == 0:
            # forward iteration
            temp = self.head
            while True:
                temp.show()
                temp = temp.next

                if temp == self.head:
                    break

        else:
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous

                if temp == self.tail:
                    break

    # Weekend Assignment

    # Add at head
    def insert(self, song):
        if self.head is None:
            self.head = song
            self.tail = song
        else:
            song.previous = self.head.previous
            self.head.previous = song
            song.next = self.head
            self.head = song

    def delete(self, track1):
        if self.head is None:
            print("The playlist is empty")
        elif self.head.track == track1:
            # If the song to be deleted is the head of the playlist
            if self.head.next == self.head:
                # Only one song in the playlist
                self.head = None
                self.tail = None
            else:
                self.head.next.previous = self.head.previous
                self.tail.next = self.head.next
                self.head = self.head.next

                # self.head = self.head.next
                # self.tail.next = self.head
                # self.head.previous = self.tail

        else:
            current_song = self.head.next
            while current_song != self.head:
                if current_song.track == track1:
                    current_song.previous.next = current_song.next
                    current_song.next.previous = current_song.previous
                    break
                current_song = current_song.next
            else:
                print("Song not found in the playlist")


# from sess8A import Song, Playlist


def main():
    play_list = Playlist()
    # print("Playlist:", play_list, vars(play_list))

    play_list.append(song=Song(track="1. Udd Jaa Kaale Kaava", artists="Udit Narayan, Alka Yagnik", duration=4.48))

    # print("Playlist:", play_list, vars(play_list))

    song2 = Song(track="2. Gustakhiyan", artists="Gurnam Bhullar", duration=3.5)
    play_list.append(song=song2)

    song3 = Song(track="3. Desperado", artists="Raghav, Tesher", duration=5.6)
    play_list.append(song=song3)

    play_list.append(
        song=Song(track="4. Chorni", artists="DIVINE, Sidhu Moose Wala", duration=4.12)
    )

    play_list.append(song=Song(track="5. Kasol", artists="Mani Longia, Starboy X", duration=2.28))

    # print("PlayList:", play_list, vars(play_list))
    #
    # print("PRINTING PLAYLIST - FORWARD")
    # play_list.iterate()
    #
    # print("PRINTING PLAYLIST - BACKWARD")
    # play_list.iterate(1)

    # play_list.insert(Song(track="Inserted-> lovely", artists="DIVINE, Sidhu Moose Wala", duration=4.12))
    # print("PRINTING PLAYLIST- after insert operation - FORWARD")
    # play_list.iterate()

    song = Song(track="Inserted-> lovely", artists="DIVINE, Sidhu Moose Wala", duration=4.12)
    play_list.insert(song)
    play_list.delete(track1="Inserted-> lovely")
    print("PRINTING PLAYLIST -after delete operation - FORWARD")
    play_list.iterate()


if __name__ == "__main__":
    main()

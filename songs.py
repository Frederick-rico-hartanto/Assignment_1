"""
Replace the contents of this module docstring with your own details
Name: Frederick Rico Hartanto
Date started: 6 August 2022
GitHub URL:
"""
print("Songs to Learn 1.0 - by Frederick Rico Hartanto")

def main():
    """..."""
    songs = [["Somebody That I Used to Know", "Gotye featuring Kimbra", "2012", "u"],
             ["Heartbreak Hotel", "Elvis Presley", "1956", "u"],
             ["Macarena", "Los Del Rio", "1996", "l"],
             ["I Want to Hold Your Hand", "The Beatles", "1964", "u"],
             ["Boom Boom Pow", "The Black Eyed Peas", "2009", "u"],
             ["My Sharona", "The Knack", "1979", "l"]
             ]

    MENU = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""

    space = " "

    print(f"{len(songs)} songs loaded")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L" or choice == "1":
            count = 0
            count_2 = 0
            for i in range(len(songs)):
                song_name = songs[i][0] + space * (30 - len(songs[i][0]))
                band = songs[i][1] + space * (25 - len(songs[i][1]))
                if songs[i][3] == "l":
                    learnt = " "
                else:
                    learnt = "*"
                print(f"{i}. {learnt} {song_name} - {band} {songs[i][2]}")
            for i in range(len(songs)):
                if songs[i][3] == "l":
                    count += 1
                if songs[i][3] == "u":
                    count_2 += 1
            print(f"{count} songs learned, {count_2} songs still to learn")
            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "A" or choice == "2":
            new_songs = []
            title = str(input("Title:"))
            while title == "":
                print("Input can not be blank")
                title = str(input("Title:"))
            else:
                new_songs.append(title)

            artist = str(input("Artist:"))
            while artist == "":
                print("Input can not be blank")
                artist = str(input("Artist:"))
            else:
                new_songs.append(artist)

            year = input("Year: ")
            valid_year = get_valid_year(year, 0)
            while not valid_year:
                year = input("Year: ")
                valid_year = get_valid_year(year, 0)

            new_songs.append(str(year))
            new_songs.append("u")
            print(f"{title} by {artist}  ({str(year)}) added to song list")
            songs.append(new_songs)
            file = open("songs.csv", "a")
            file.write("\n")
            file.write(','.join(new_songs))
            file.close()
            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "C" or choice == "3":
            all_learnt = False
            for i in range(len(songs)):
                if songs[i][-1] == "u":
                    all_learnt = True
            if all_learnt == True:
                completion = input("Enter the number of a song to mark as learned: ")
                valid_inputs = get_valid_number(completion, songs)
                while not valid_inputs:
                    completion = input("Enter the number of a song to mark as learned: ")
                    valid_inputs = get_valid_number(completion, songs)

                if songs[int(completion)][-1] == "l":
                    print(f"You have already learned {''.join(songs[int(completion)][0])}")
                else:
                    songs[int(completion)][-1] = "l"
                    print(f"{' '.join(songs[int(completion)][:-1])} learned")
            else:
                print("No more songs to learn!")

            # with open('songs.csv', 'r') as file:
            #     data = file.readlines()
            #
            # for i in range(len(songs)):
            #     data[i] =
            #
            # with open('songs.csv', 'w') as file:
            #     file.writelines(data)
            file = open("songs.csv", "r")
            replacement = ""
            # using the for loop
            for i in range(len(songs)):
                if songs[i][3] == "l":
                    for line in file:
                        line = line.strip()
                        changes = line.replace("u", "l")
                        replacement = replacement + changes + "\n"
            file.close()
                    # opening the file in write mode
            fout = open("songs.csv", "w")
            fout.write(replacement)
            fout.close()

            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid menu choice")
            print(MENU)
            choice = input(">>> ").upper()

    print("Have a nice day :)")


def get_valid_year(year, low):
    try:
        if int(year) < low:
            print("Number must be >= 0")
            return False
        else:
            return True

    except ValueError:
        print("Invalid input; enter a valid number")
        return False

def get_valid_number(completion, songs):
    try:
        if int(completion) < 0:
            print("Number must be >= 0")
            return False

        if int(completion) > len(songs):
            print("Invalid song number")
            return False

        else:
            return True

    except ValueError:
        print("Invalid input; enter a valid number")
        return False

main()
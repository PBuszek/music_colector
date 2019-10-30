from music_reports import *


def menu():
    print()
    print("""****** MENU ******
[1] View all imported albums
[2] Find all albums by genre
[3] Find all albums from given time range
[4] Find shortest / longest album
[5] Find all albums created by given artist""")


def user_input():
    while True:
        print()
        user_input = input('Choose a menu or press "b" to main menu: ')
        if user_input == "1":
            print(all_albums("text_albums_data.txt"))
        elif user_input == "2":
            parameter = input("Please enter a genre: ")
            print(albums_by_genre("text_albums_data.txt", parameter))
        elif user_input == "3":
            year1 = int(input("Please enter a starting year: "))
            year2 = int(input("Please enter the ending year: "))
            print(albums_by_time_range("text_albums_data.txt", year1, year2))
        elif user_input == "4":
            parameter = input("Do you wish the shortest or longest album? ")
            print(shortest_longest_album("text_albums_data.txt", parameter))
        elif user_input == "5":
            artist = input("Please enter an artist name: ")
            print(find_albums_by_artist("text_albums_data.txt", artist))
        elif user_input == "b":
            menu()


def main():
    menu()
    user_input()


main()

#kurwa nie działa
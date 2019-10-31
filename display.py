#TODO:
#1/ po wybraniu opcji dodanie informacji co tak naprawdę zostanie wypisanie. 
# coś w rodzaju: "All imported albums: (i pod spodem lista)". 
# W opcji [2] - "All <genre> albums: ", 
#dla [3] "Albums released beteween <start> and <end>: ", "The longest album: < album> (i może jego długość)" 
#
#2/ W opcji [2], [4] i [5] nie wiem co mam wpisać!!!!. Rozważyłbym, żeby po wybraniu tych opcji z menu, wypisać możliwe opcje do wyboru, np:
#"Select one of the below genres or "b" to go back to main menu:
#[1] pop
#[2] rock
#[3] ...
#
#Albo
#"Which album do you wish: 
#[s] - shortest
#[l] - longest
#
#3/ Przed przekazaniem dalej wpisanej przez użytkownika wartości - zawsze bym jest stripował, bo jak np. w opcji [5] wpiszę "Monika Brodka " 
#(ze spacją) to nic nie zwróci... A w opcji 4 moznaby dla urozmaicenia obsłużyć możliwość wpisania zarówno "s" jak i "shortest".
#
#4/ jesli oczekuje, że uzytkownik wpisze liczbę to musze rozważyć uzycie try/except celem wyłapania wyjątku. 
#Jesli np. wpiszę "noga" zapytany o rok - to aplikacja się wywala.
#
#5/ W menu przydałaby sie opcja do wyjścia z aplikacji.
#
#6/ To kwestia dyskusyjna, ale... skoro za każdym razem otwieram i wczytuje plik to możena by zrobić czy nie byłoby 
#lepiej wczytać go raz na początku i później tylko operować na tej tablicy tablic.


from music_colector2 import*




def menu():
    print("\n")
    print("""     ****** MENU ******
{1} View all imported albums
{2} Find all albums by genre
{3} Find all albums from given time range
{4} Find shortest / longest album
{5} Find all albums created by given artist
{b} Press if you want break and exit""")
    "\n"


def user_input():

    location_of_file = "/home/przemek/Pulpit/music_colector/text_albums_data.txt"                        #wrzuć swój adres pliku

    #data = read_albums(location_of_file)


    is_running = True
    while is_running:
        print("\n")
        user_input = input('Choose a menu or press "0" to main menu: ')
        if user_input == "1":
            print("\n")
            print("All imported albums:")
            print(find_all_albums(location_of_file))
            print("\n")
        elif user_input == "2":
            print("\n")
            parameter = input("Please enter a genre: ")
            print(f'All albums by {parameter}:')
            print(find_albums_by_genre(location_of_file, parameter))
            print("\n")
        elif user_input == "3":
            print("\n")
            print("All albums by given time range:")
            year1 = int(input("Please enter a starting year: "))
            year2 = int(input("Please enter the ending year: "))
            print(f'All albums from {year1} years to {year2} years:')
            print(find_albums_by_time_range(location_of_file, year1, year2))
            print("\n")
        elif user_input == "4":
            print("\n")
            parameter = input("Do you wish the shortest or longest album? ")
            print(f'All albums sorted by {parameter}')
            print(find_shortest_longest_album(location_of_file, parameter))
            print("\n")
        elif user_input == "5":
            print("\n")
            artist = input("Please enter an artist name: ")
            print("All albums by given artist:")
            print(find_albums_by_artist(location_of_file, artist))
            print("\n")
        elif user_input == "0":
            menu()
        elif user_input == "b":
            is_running = False


def main(): 
    #ocation_of_file = "/home/przemek/Pulpit/music_colector/text_albums_data.txt"
    #print(test_music_colector.file_name(location_of_file))
    menu()
    user_input()


main()


main()

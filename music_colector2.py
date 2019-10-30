def all_albums(file_name):
    all_albums = []
    with open(file_name, "text_albums_data.txt") as file:
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            all_albums.append(all_info[1])
        return "\n".join(all_albums)

def albums_by_genre(file_name, genre):
    genres_dictionary = {}
    albums = []
    with open(file_name, "text_albums_data.txt") as file:
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            genres_dictionary[all_info[1]] = all_info[3]
        for key, value in genres_dictionary.items():
            if value == genre:
                albums.append(key)
        return "\n".join(all_albums)

def albums_by_time_range(file_name, year1, year2):
    albums_dictionary = {}
    albums = []
    with open(file_name, "text_albums_data.txt") as file:
        for line in line:
            all_info = line.strip()
            all_info = all_info.split(",")
            albums_dictionary[all_info[1]] = int(all_info[2])
        for key, value in albums_dictionary.items():
            if value >= year1 and value <= year2:
                albums.append(key)
        return "\n".join(all_albums)

def schortest_longest_album(file_name, parametr):
    with open(file_name, "text_albums_data.txt"):
        albums = []
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            all_info = all_info.replace(":", ".")
            albums.append((float(all_info[4])))
        if parametr == "schortest":
            albums = sorted(albums)
            return albums[0][1]
        if parametr == "longest":
            albums = sorted(albums, reverse=True)
            return albums[0][1]


def find_albums_by_artist(file_name, artist):
    with open(file_name, "text_albums_data.txt") as file:
        albums_dictionary ={}
        albums = []
        for line in file:
            all_info = line.strip()
            all_info = all_info.replace(":", ".")
            all_info = all_info.split(",")
            albums_dictionary[all_info[1]] = all_info[0]
        for key, value in albums_dictionary.items():
            if value == artist:
                albums.append(key)
        return "\n".join(albums)



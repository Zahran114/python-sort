def selection_sort_players(list_of_players):
    n = len(list_of_players)
    for i in range(n-1):
        
        max_index = i
        for j in range(i+1, n):
            if list_of_players[j]["Jumlah Gol"] > list_of_players[max_index]["Jumlah Gol"]:
                max_index = j

        
        list_of_players[i], list_of_players[max_index] = list_of_players[max_index], list_of_players[i]

    return list_of_players


list_of_players = [
    {"No.": 1, "Nama Pemain": "Kylian Mbappe", "Klub": "Paris Saint Germain", "Jumlah Gol": 40},
    {"No.": 2, "Nama Pemain": "Victor Osimhen", "Klub": "Napoli", "Jumlah Gol": 28},
    {"No.": 3, "Nama Pemain": "Robert Lewandowski", "Klub": "Barcelona", "Jumlah Gol": 33},
    {"No.": 4, "Nama Pemain": "Erling Haaland", "Klub": " ", "Jumlah Gol": 52},
    {"No.": 5, "Nama Pemain": "Christopher Nkunku", "Klub": "RB Leipzig", "Jumlah Gol": 22},
]


sorted_player_list = selection_sort_players(list_of_players)


print("Daftar pemain terurut berdasarkan jumlah gol:")
for player in sorted_player_list:
    print("No.:", player["No."])
    print("Nama Pemain:", player["Nama Pemain"])
    print("Klub:", player["Klub"])
    print("Jumlah Gol:", player["Jumlah Gol"])
    print()

def are_you_playing_banjo(name:str):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"
    




print(are_you_playing_banjo("Roma"))


print(are_you_playing_banjo("Vova"))


print(are_you_playing_banjo("roma"))
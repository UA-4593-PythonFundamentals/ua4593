def playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} playing banjo"
    else:
        return f"{name} not playing banjo"

print(playing_banjo("Robert"))
print(playing_banjo("Alice"))
print(playing_banjo("Randy"))
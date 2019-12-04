characters = {}

keyboardInput = input()

for i in keyboardInput:
    characters.setdefault(i,0)
    characters[i] += 1

print(characters)

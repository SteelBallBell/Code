string = "aeiouxyz"

def strong(string):
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            return True
        else:
            return False

print(strong(string))

# I asked AI for the puzzle and then it said it didnt work as intended lol
# this is regardless of the fact that it works💀💀.
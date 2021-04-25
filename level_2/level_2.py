names_dict = dict()

with open('names.txt', 'r') as f:
    for name in f:
        s = 0
        for char in name:
            if char != '\n':
                s += ord(char)
        names_dict[s] = name

print(names_dict[max(names_dict.keys())])

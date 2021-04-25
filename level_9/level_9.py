message_dict = dict()

with open('message.txt', 'r') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        splited_line = line.split()

        length = len(splited_line)
        if length == 2:
            splited_line[-1] = ' '
        if length >= 2:
            message_dict.update({int(splited_line[0]): splited_line[-1]})

message = ''
for key in sorted(message_dict.keys()):
    message += message_dict[key]

print(message)
print(len(message))

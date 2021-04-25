import re

valid_passwords = list()

with open('passwords.txt', 'r') as f:
    for passwd in f:
        if passwd[-1] == '\n':
            passwd = passwd[:-1]

        if re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{8,}$', passwd):
            valid_passwords.append(passwd)

print(len(valid_passwords), valid_passwords)

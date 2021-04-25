prev_statement = '11'
statement_42 = ''

for n in range(3, 43):
    n_stament = ''

    for i in range(0, len(prev_statement)):
        if i == 0:
            counter = 1
        else:
            if prev_statement[i] == prev_statement[i - 1]:
                counter += 1
            else:
                n_stament += str(counter)
                n_stament += prev_statement[i - 1]
                counter = 1

    n_stament += str(counter)
    n_stament += prev_statement[i]
    prev_statement = n_stament

print(f'n={n}', len(n_stament))

import math

x0 = y0 = 0
axis = 'x'
head = 'up'

with open('commands.txt', 'r') as f:
    for command_line in f:

        if command_line[-1] == '\n':
            command_line = command_line[:-1]

        direction = command_line[0]
        meter = int(command_line[1:])

        if head == 'up':
            if axis == 'x' and direction == 'L' or axis == 'y' and direction == 'R':
                head = 'down'

            if axis == 'x':
                x0 = x0 + meter if direction == 'R' else x0 - meter
                axis = 'y'

            elif axis == 'y':
                y0 = y0 - meter if direction == 'R' else y0 + meter
                axis = 'x'

        elif head == 'down':
            if axis == 'x' and direction == 'L' or axis == 'y' and direction == 'R':
                head = 'up'

            if axis == 'x':
                x0 = x0 - meter if direction == 'R' else x0 + meter
                axis = 'y'

            elif axis == 'y':
                y0 = y0 + meter if direction == 'R' else y0 - meter
                axis = 'x'

print(math.sqrt(x0 ** 2 + y0 ** 2))

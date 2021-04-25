converted_message = list()


def get_char(digit, counter):
    if digit == '1':
        chars_list = ['']
    elif digit == '2':
        chars_list = ['a', 'b', 'c']
    elif digit == '3':
        chars_list = ['d', 'e', 'f']
    elif digit == '4':
        chars_list = ['g', 'h', 'i']
    elif digit == '5':
        chars_list = ['j', 'k', 'l']
    elif digit == '6':
        chars_list = ['m', 'n', 'o']
    elif digit == '7':
        chars_list = ['p', 'q', 'r', 's']
    elif digit == '8':
        chars_list = ['t', 'u', 'v']
    elif digit == '9':
        chars_list = ['w', 'x', 'y', 'z']

    return chars_list[counter - 1]


with open('numbers.txt', 'r') as f:
    for longnum in f:

        for word_in_num in longnum.split('0'):
            converted_word = ''
            counter = 1
            length = len(word_in_num)

            for index in range(1, length):

                if word_in_num[index] == word_in_num[index - 1]:
                    counter += 1
                else:
                    converted_word += get_char(word_in_num[index - 1], counter)
                    counter = 1

                if index + 1 == length:
                    converted_word += get_char(word_in_num[index], counter)

            converted_message.append(converted_word)

print(' '.join(converted_message))

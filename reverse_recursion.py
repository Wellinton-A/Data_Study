def reverse_string(str):
    if str == '':
        return ''
    return reverse_string(str[1:]) + str[0]

print(reverse_string('Wellinton'))
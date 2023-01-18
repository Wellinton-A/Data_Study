
# list2.insert('a')

# print(list2)
# Reverse a string

phrase = "meu nome"
def reverse_string(string):
    if not isinstance(string, str):
        return f'\'{string}\' is a {type(string)}'
    li = [l for l in string]
    li_ = li[::-1]
    return ''.join(li_)

phrase = reverse_string(phrase)

print(phrase)


list1 = [0,2,4,6,8]
list2 = [1,3,5,7,9]

def merger_sort_list(li: list, li2: list):
    li.extend(li2)
    return sorted(li)

print(merger_sort_list(list1, list2))

        
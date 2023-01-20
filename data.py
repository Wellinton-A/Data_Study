
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
    return list.sort(li)

print(merger_sort_list(list1, list2))


print(list1.pop())
print(list2)
        

dict1 = {
    'age': 54,
    'name': 'Wellinton'
}


list10 = [2,5,1,8,3,10,11,9,2]
list20 = [2,1,1,2,3,5,1,2,4]
list30 = [2,3,4,5]

def first_recurring_character2(li: list):
    repeat = len(li)
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                if j < repeat:
                    repeat = j
    if repeat == len(li):
        return None
    return li[repeat]  

def first_recurring_character(li: list):
    dict = {}
    for i in li:
        if not dict.get(i):
            dict.update({i: True})
        else:
            return i


                

print(first_recurring_character(list10))
print(first_recurring_character(list20))
print(first_recurring_character(list30))

print(first_recurring_character2(list10))
print(first_recurring_character2(list20))
print(first_recurring_character2(list30))

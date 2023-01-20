
def reverse_string(text: str):
    letter_list = [word for word in text]
    return ''.join(reversed(letter_list))
    

text1 = "This code uses a defaultdict(int), which is a subclass of the built-in dict class in Python that returns a default value of 0 for nonexistent keys. This allows us to increment the count for a word without first having to check if it's already in the hash table. The code takes a string of text, split it into list of words and count the occurrences of each word by keeping track of the count in the hash table and finally it prints the result."

print(reverse_string(text1))

def letter_count2(text: str,):
    word_list = []
    for i in text:
        if i != ' ':
            word_list.append(i)
    return word_list

print(letter_count2(text1))

def word_count(text: str):
    words = 0
    word_list = text.split()
    for i in word_list:
        words += 1
    return word_list

print(word_count(text1))


    
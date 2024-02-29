def longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

words = ['мама', 'папа', 'кот', 'паровоз']
print(longest_word(words))


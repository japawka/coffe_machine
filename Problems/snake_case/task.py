word = input()
new_word = ''
for letter in word:
    if letter.isupper():
        letter = '_' + letter.lower()
    new_word += letter
print(new_word)

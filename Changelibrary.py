import os

file = os.getcwd()
file += "\\russian_nouns.txt"
file_2 = os.getcwd()
file_2 += "\\russian_nouns_5_letters.txt"

print("Trying to open: ", file)

five_letter_words = []
with open(file, encoding='utf-8') as ruslib:
    words = list(ruslib.read().split("\n"))
    for word in words:
        if len(word) == 5:
            five_letter_words.append(word)

with open(file_2, "w", encoding='utf-8') as new_file:
    for word in five_letter_words:
        new_file.write(word + "\n")

with open(file_2, encoding='utf-8') as file:
    words = list(file.read().split("\n"))
    print(*words, sep="\n")


import os


def count_l(letter, words):
    count = 0
    for word in words:
        if letter in word:
            count += 1
    return count


def letters_in(letters, game_words):
    sl_words = []
    for word in game_words:
        if (letters | set(word)) == set(word):
            sl_words.append(word)
    return sl_words


def letters_out(letters, game_words):
    ex_words = []
    for word in game_words:
        if len(letters & set(word)) == 0:
            ex_words.append(word)
    return ex_words


def letters_in_positions(l_pos, game_words):
    pos_words = []
    for word in game_words:
        check = 0
        for i in range(5):
            if l_pos[i] == "_" or l_pos[i] == word[i]:
                check += 1
        if check == 5:
            pos_words.append(word)
    return pos_words


def letters_not_in_positions(not_l_pos, game_words):
    pos_words = []
    for word in game_words:
        check = 1
        for not_pos in not_l_pos:
            for i in range(5):
                if not_pos[i] == word[i]:
                    check = 0
                    break
        else:
            if check:
                pos_words.append(word)
    return pos_words


def best_word(words, letters_frq):
    best_words = {}
    for word in words:
        frq = 0
        for i in set(word):
            frq += letters_frq[i]
        best_words[word] = frq
    sorted_words = list(sorted(best_words.keys(), key=lambda x: best_words[x], reverse=True))
    return sorted_words


def play_game(words, letters_frq):
    num_tries = 1
    game_words = words
    letters_incl = set()
    letters_ex = set()
    letter_pos = ['_', '_', '_', '_', '_']
    not_letter_pos = []
    while len(game_words) > 1:
        print(f"{num_tries} try to guess your five letter word. Is it: ", end="")
        game_words = best_word(game_words, letters_frq)
        suggested_word = game_words[0]
        print(f"{suggested_word}?\nIt can also be one of {len(game_words) - 1} words like: ", end="")
        print(*game_words[1:20], sep=", ")
        l_in = input("Print letters which are in your word: ")
        for v in l_in:
            letters_incl.add(v)
        print("Letters in your word: ", letters_incl)
        game_words = letters_in(letters_incl, game_words)
        if len(game_words) == 1:
            print("your word is: ", game_words[0], "; Tries to guess: ", num_tries + 1, sep='')
            break
        for v in suggested_word:
            if v not in l_in:
                letters_ex.add(v)
        print("Letters not in your word: ", letters_ex)
        game_words = letters_out(letters_ex, game_words)
        if len(game_words) == 1:
            print("your word is: ", game_words[0], "; Tries to guess: ", num_tries + 1, sep='')
            break
        l_pos = input("Print letters on right positions, separated by _ if no letter in position: ")
        if l_pos == suggested_word:
            print("That was your word!", num_tries)
            break
        for i in range(5):
            if letter_pos[i] == "_" and l_pos[i] != "_":
                letter_pos[i] = l_pos[i]
        print("Current word looks like: ", letter_pos)
        game_words = letters_in_positions(letter_pos, game_words)
        for k in range(5):
            if suggested_word[k] not in letter_pos and suggested_word[k] not in letters_ex:
                tmp = ['_', '_', '_', '_', '_']
                tmp[k] = suggested_word[k]
                not_letter_pos.append(tmp)
        game_words = letters_not_in_positions(not_letter_pos, game_words)
        num_tries += 1
    else:
        if len(game_words) == 1:
            print("your word is: ", game_words[0], "; Tries to guess: ", num_tries)
        else:
            print(f"you made a mistake playing this game: \n"
                  f"your word looks like {letter_pos}\n"
                  f"letters in your word {letters_incl}\n"
                  f"letters not in your word: {letters_ex}")


def main():
    directory = os.getcwd()

    file_w = directory + "\\russian_nouns_5_letters.txt"
    with open(file_w, encoding='utf-8') as file:
        words = list(file.read().split("\n"))
        if len(words[-1]) != 5:
            words.pop()

    file_l = directory + "\\russian_letters_frq.txt"
    with open(file_l, encoding='utf-8') as file:
        letters = list(file.read().split("\n"))
        letters_frq = {}
        for letter in letters:
            k, v = letter.split()
            letters_frq[k] = int(v)
            # letters_frq[k] = count_l(k, words)
    play_game(words, letters_frq)


if __name__ == "__main__":
    main()

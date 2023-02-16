import random
lst = ["bmw", "fait", "kiaa", "mercedes"]


def get_user_name():
    name = input("input your username : ")
    if any(chr.isdigit() for chr in  name) or not name:
        print(" not a valid user name ")
        name = get_user_name()
    return name


def hangman():
    indx = random.randint(0, len(lst)-1)  # pick a random word
    picked_word = lst[indx]
    name = get_user_name()
    len_of_picked_word =  len(picked_word)

    # keep track of number of counts alongs with the final res
    tmpCNt, maxTmp, res = 0, 10, ["-"] * len_of_picked_word

    for i in range(maxTmp):
        tmpChr = input(f'guess the {tmpCNt+1} chr at ur char : ')
        if tmpChr in picked_word:
            res[picked_word.index(tmpChr)] = tmpChr
            print("".join(res))
            tmpCNt += 1
            if tmpCNt == len_of_picked_word: #reach the end
                print(f"winners winners chicken dinners, U get through it after {i} times")
                return 
        else:
            print(f'your char not included !')

    else :
        print("Try Again !")


hangman()

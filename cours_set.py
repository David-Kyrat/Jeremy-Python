def intro():
    listdbl = [2, 2, 3]
    l = ["2", "3", "4"]
    s = set()

    for el in listdbl:
        print(f"adding {el} to set: {s}")
        s.add(el)
        print(f"set={s}\n")

    print(",".join(l))  # pas faire ",".join(listdbl) car c'est pas une liste de string (str) !


def clean(text, toRemove):
    cleanText = text
    for charToRemove in toRemove:
        cleanText = cleanText.replace(charToRemove, "")
    return cleanText

def extract_diff_word(wordlist):
    s1 = set()
    for word in wordlist:
        s1.add(word)
    return s1

def count_occurences(text):
    toRemove = [':', ';', ',', '.', "(", ")", "\""]
    wordlist = clean(text, toRemove).split(" ")
    s1 = extract_diff_word(wordlist)
    
    occurences = {}
    for word in s1:
        occurences[word] = wordlist.count(word)

    return occurences
    

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

occurences = count_occurences(text)
print(occurences)

set(occurences.keys()) # return toutes les clés (ici: tous les mots)


def common_words(text1, text2):
    toRemove = [':', ';', ',', '.', "(", ")", "\""]
    wordlist1 = clean(text1, toRemove).split(" ")
    wordlist2 = clean(text2, toRemove).split(" ")

    s1, s2 = extract_diff_word(wordlist1), extract_diff_word(wordlist2)
    return s1.intersection(s2)

print(common_words(text, text))

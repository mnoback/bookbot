def wordcount(text):
    textsplit = text.split()
    num_words = len(textsplit)
    print(f"Found {num_words} total words")

def charcount(text):
    lctext=text.lower()
    chars = {}
    for char in lctext:
        if (char in chars)==False:
            chars[char]=0
        chars[char]+=1
    return chars

def charsplit(dict):
    dict2 = []
    for entry in dict:
        if entry.isalpha()==True:
            dictadd = {"char": entry, "num": dict[entry]}
            dict2.append(dictadd)

    return dict2

def charsort(dict):
    return dict["num"]

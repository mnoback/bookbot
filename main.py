import sys
print(sys.argv)
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
bookpath=sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents
    
from stats import wordcount
from stats import charcount
from stats import charsplit
from stats import charsort

def main():
    f = get_book_text(bookpath)
    
    charcount(f)
    charsplit(charcount(f))
    output = charsplit(charcount(f))
    output.sort(key=charsort,reverse=True)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    wordcount(f)
    print("--------- Character Count -------")
    for char in output:
        print(f"{char["char"]}: {char["num"]}")

main()
print(sys.argv)
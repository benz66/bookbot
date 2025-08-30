import sys
from stats import num_words, character_count, sort_on, sort_reverse

if len(sys.argv) != 2:
    print("- 'Usage: python3 main.py <path_to_book>'")
    sys.exit(1)
else:
    book = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents 

def main():
    contents = get_book_text(book)
    words = num_words(contents)
    print(f"Found {words} total words")
    count = character_count(contents.lower())
    #print(count)
    output = sort_reverse(count)
    for item in output:
        print(f"{item['char']}: {item['num']}")

main()

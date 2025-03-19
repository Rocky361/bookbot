import sys
from stats import count_words, count_characters, sorted_list_of_dictionaries

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path) 
    num_words = count_words(text)
    char_counts = count_characters(text)
    dictionaries = sorted_list_of_dictionaries(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in dictionaries:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 



main()
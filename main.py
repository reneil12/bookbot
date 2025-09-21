import sys
from stats import get_num_words, get_character_count, get_character_count_list, sort_on

def main():
   try:
       book = sys.argv[1]
       book_text = get_book_text(book)
   except Exception as e:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   text_count = get_num_words(book_text)
   character_count = get_character_count(book_text)
   character_count_list = get_character_count_list(character_count)
   character_count_list.sort(reverse=True, key=sort_on)
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book}...")
   print("----------- Word Count ----------")
   print(f"Found {text_count} total words")
   print("--------- Character Count -------")
   for dic in character_count_list:
       print(f"{dic["char"]}: {dic["num"]}")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
main()
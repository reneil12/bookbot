def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    character_count = {}
    for character in book_text:
        lowered = character.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

def get_character_count_list(character_count):
    sorted_count = []
    for k, v in character_count.items():
        sorted = {}
        sorted["char"] = k
        sorted["num"] = v
        sorted_count.append(sorted)
    return sorted_count

def sort_on(items):
    return items["num"]

        
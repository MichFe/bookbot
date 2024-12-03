def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)

    print(f"--- Begining report of {book_path}")

    book_words = count_words(book_text)
    print(f"{book_words} words found in the document\n")

    book_characters = count_characters(book_text)
    sorted_list = sort_dict(book_characters)

    for char_count in sorted_list:
        if not char_count["name"].isalpha():
            continue
        print(f"The '{char_count['name']}' character was found {char_count['count']} times")

    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def sort_on(dict):
    return dict['count']

def sort_dict(dict):
    char_list = []
    for key in dict:
        char_list.append({"name": key, "count": dict[key]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list




main()

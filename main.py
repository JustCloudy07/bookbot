def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_dict = count_characters(text)
    list_char_dict = dictionary_to_listofdictionaries(char_dict)
    print(text)
    print("\n")
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} word(s) found in the document")
    print("\n\n")
    for character in list_char_dict:
        print(f"The '{character['char']}' character was found '{character['num']}' times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_array = text.split()
    return len(word_array)

def count_characters(text):
    character_dictionary = {}
    lowered_text = text.lower()

    for character in lowered_text:
        if (character in character_dictionary):
             character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary

def sort_on(dict):
    return dict["num"]

def dictionary_to_listofdictionaries(dict):
    dictionary_list = []
    for character in dict:
        if character.isalpha():
            dictionary_list.append({"char": character, "num": dict[character]})
        else:
            continue
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

main()
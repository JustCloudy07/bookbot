def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    character_dict = dict()
    lower_case = book_text.lower()
    for character in lower_case:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    
    return character_dict

def sort_on(dict):
    return dict["count"]
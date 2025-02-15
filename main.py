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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of document ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        char_dict = count_characters(file_contents)

        list_dict = []
        for character in char_dict:
            if character.isalpha():
                list_dict.append({"character": character, "count": char_dict[character]})
        list_dict.sort(reverse=True, key=sort_on)

        for item in list_dict:
            print(f"The '{item["character"]}' character was found {item["count"]} times")
        print("--- End report ---")
        
        
                

main()


from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open((sys.argv)[1]) as f:
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
            print(f"{item["character"]}: {item["count"]}")
        print("--- End report ---")
        
        
                

main()


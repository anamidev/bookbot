import sys

def count_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def count_letters(text):
    char_dict = {}
    for char in text:
        char_lowered = char.lower()
        if not char_lowered in char_dict:
            char_dict[char_lowered] = 1
        else:
            char_dict[char_lowered] += 1

    char_list = []
    for prop in char_dict:
        if prop.isalpha():
            char_list.append({"character": prop, "occurrence":char_dict[prop]})

    char_list.sort(reverse=True, key=sort_on)

    for i in range(0,len(char_list)):
        print(f"The '{char_list[i]["character"]}' character was found {char_list[i]["occurrence"]} times")

def sort_on(dict):
    return dict["occurrence"]

def main():
    try:
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = "./books/frankenstein.txt"

        with open(file_path) as f:
            file_contents = f.read()
            print(f"--- Begin report of {file_path} ---")
            count_words(file_contents)
            print("")
            count_letters(file_contents)
            print("--- End report ---")
            
    except Exception as e:
        print(e)
main()
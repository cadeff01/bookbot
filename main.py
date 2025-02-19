def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    count = char_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)}  words found in the document\n")
    for char, count in count:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def word_count(contents):
    words = contents.split()
    return len(words)


def char_count(contents):
    dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for char in contents.lower():
        if char in dict:
            dict[char] += 1
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict


main()

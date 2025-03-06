from stats import word_counter, char_counter, sorted_char_list, format
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        fileContent = f.read()

    return fileContent

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    words = word_counter(get_book_text(path))
    chars = char_counter(get_book_text(path))
    sorted_chars = sorted_char_list(chars)
    format(path, words, sorted_chars)

if __name__ == "__main__":
    main()
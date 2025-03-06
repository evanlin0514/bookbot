def word_counter(content):
    words = content.split()
    return f"Found {len(words)} total words"

def char_counter(content):
    content = content.lower()
    result = {}
    for i in content:
        if i not in result:
            result[i] = 1
            continue
        result[i] += 1
    
    return result

def sorted_char_list(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({'char': char, 'count': count})

    sorted_list = sorted(sorted_list, key = lambda item: item['count'], reverse = True)
    return sorted_list

def format(path, words, char_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    print(f"----------- Word Count ----------\n{words}\n--------- Character Count -------")
    for char in char_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['count']}")    
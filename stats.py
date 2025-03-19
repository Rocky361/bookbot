def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_case_text = text.lower()
    char_counts = {}
    for char in lower_case_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_on(d):
    return d["count"]

def sorted_list_of_dictionaries(char_count):
    result = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count" : count}
        result.append(char_dict)
    
    result.sort(reverse=True, key=sort_on)
    
    return result
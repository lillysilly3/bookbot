def get_num_words(text):
    # Counts words of the text
    words = text.split()
    return len(words)

def get_character_counts(text):
    # Counts how many times every character was used in the text
    counts = {}
    text = text.lower() 

    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    
    return counts

def character_sorted(character_count):
    # Sorts get_character_counts dictionary by highest number of use but only for alphabetical character
    sorted_list = []
    
    for key, value in character_count.items():
        if key.isalpha():
           sorted_list.append({"char": key, "num": value})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(item):
    return item["num"]


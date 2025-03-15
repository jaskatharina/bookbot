def num_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    freq_dict = {}
        
    for char in book_text:
        try:
            freq_dict[char.lower()] += 1
        except KeyError:
            freq_dict[char.lower()] = 1

    return freq_dict

def sort_on(dict):
    return dict["count"]

def format_dict(freq_dict):
    dicts_list = []
    for key in freq_dict:
        dicts_list.append({"character": key, "count": freq_dict[key]})
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list
    
        

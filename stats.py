def word_count(contents):
    return len(contents.split())

def char_count(contents):
    char_stats = {}

    for char in contents.lower():
        if char in char_stats:
            char_stats[char] += 1
        else:
            char_stats[char] = 1
    
    return char_stats
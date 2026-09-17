def break_words(stuff):
    """分割字符串"""
    words = stuff.split(" ")
    return words

def sort_words(words):
    '''字符串排序'''
    return sorted(words)

def print_first_word(words):
    '''删除字符串第一个'''
    word = words.pop(0)
    print(word)

def print_last_word(words):
    '''删除字符串最后一个'''
    word = words.pop(-1)    
    print(word)

def sort_sentence(sentence):
    """把字符串变成列表然后排序"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last_sorted(sentence):
    """字符串排序变成列表返回第一个和最后一个"""
    #word = break_words(sentence)
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last(sentence):
    """把字符串变成列表
       返回第一个和最后一个
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    

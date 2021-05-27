'''
text: list of strings
dictionary: list of words

1. split text into length of dictionary if no set is covered then length + 1 and continue till a set is covered
2. 
'''

'["apple"]' '["apple"]'

def smallest_cover(text, dictionary):
    dictionary = set(dictionary)
    current_text = {}
    lookahead = 0
    start = 0
    min_subarray_length = len(text)
    min_subarray_idx = 0
    while lookahead < len(text):
        if len(current_text) == len(dictionary):
            if lookahead - start < min_subarray_length:
                min_subarray_length = lookahead - start
                min_subarray_idx = start
            if text[start] in current_text:
                current_text[text[start]] -= 1
                if current_text[text[start]] == 0:
                    del current_text[text[start]]
            start += 1
        else:
            if text[lookahead] in dictionary:
                if text[lookahead] not in current_text:
                    current_text[text[lookahead]] = 0
                current_text[text[lookahead]] += 1
            lookahead += 1
    
    if len(current_text) == len(dictionary):
        min_subarray_length = min(min_subarray_length, lookahead - start)
        min_subarray_idx = start
    
    return min_subarray_idx, min_subarray_length

text = 'My paramount object in this struggle is to save the Union and is not either to save or to destroy slavery. if I could save the Union without freeing any slave I would do it, and if I could save it by freeing all the slaves I would do it; and if I could save it by freeing some and leaving others alone I would also do that'.split(' ')

print(smallest_cover('apple banana apple apple dog cat apple dog banana apple cat dog'.split(' '), ['banana', 'cat']))

print(text[24:])





    
    

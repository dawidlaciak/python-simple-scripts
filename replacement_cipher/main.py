import math
from itertools import chain

def replacement_coder(text:str):

    text_length = len(text)
    required_lists = math.ceil(math.sqrt(text_length))
    encrypted_text = [['' for i in range(required_lists)] for i in range(required_lists)]
    indexed_element = 0

    for i in range(required_lists):
        for j in range(required_lists):
            if indexed_element < text_length:
                encrypted_text[j][i] = text[indexed_element]
                indexed_element += 1

    encrypting_result = ''.join(chain.from_iterable(encrypted_text))

    return encrypting_result

print(replacement_coder('W kotłowni łowi się koty.'))



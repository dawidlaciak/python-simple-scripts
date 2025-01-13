def check_subtext(text_a:str, text_b:str) -> bool:
    letter_number = 0

    text_a = text_a.lower()
    text_b = text_b.lower()
    
    for letter in text_b:

        if letter_number == len(text_a):
            break

        if text_a == ' ' or text_b == ' ':
            continue      

        if text_a[letter_number] == letter:
            letter_number += 1

    if letter_number == len(text_a):
            print(f'{text_a} is subtext of {text_b}.')
            return True
    else:
         print(f'{text_a} is not subtext of {text_b}.')
         return False

if __name__ == '__main__':
    check_subtext("def", "abcdef")
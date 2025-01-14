def metagram_checker(word1:str, word2:str) -> bool:

    if len(word1) != len(word2):
        print(f'{word1} and {word2} have different lengths, so they cannot be metagrams.')
        return False
    elif word1 == '' or word2 == '':
        print('One of the strings is empty.')
        return False

    different_letters = 0
    
    word1 = word1.lower()
    word2 = word2.lower()

    for i in range(len(word1)):

        if word1[i] != word2[i]:
            different_letters += 1

        if different_letters > 1:
            print(f'{word1} and {word2} are not metagrams.')
            return False
        
    if different_letters == 0:
        print(f'{word1} and {word2} are identical.')
        return False
    
    print(f'{word1} and {word2} are metagrams.')
    return True

if __name__ == '__main__':
    metagram_checker('kasa', 'kara')
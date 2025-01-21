def sms_converter(text:str) -> str:

    converted_text = []
    converter_dict = {}
    letter_number = ord('A')
    
    for i in range(2, 10):

        if i == 9 or i == 7:
            converter_dict[i] = [chr(letter_number+x) for x in range(4)]
            letter_number += 1
        else: 
            converter_dict[i] = [chr(letter_number+x) for x in range(3)]

        letter_number += 3

    if text.replace(' ', '').isalpha():
        text = text.upper()

        for letter in text:
            
            if letter == ' ':
                converted_text.append('0')

            for key in converter_dict:
                if letter in converter_dict[key]:
                    converted_text.append(str(key) * (converter_dict[key].index(letter) + 1))
        
        return '/'.join(converted_text)
    
    else:
        split_num = text.split('/')
        print(split_num)

        for number in split_num:
            if number == '0':
                converted_text.append(' ')
            else:
                converted_text.append(converter_dict[int(number[0])][len(number) - 1])
        
        return ''.join(converted_text)
    
    return 'Incorrect data'


if __name__ == '__main__':
    result = sms_converter('7/666/6/666/222/999/0/555/2/4/88/66/0/7777/444/33/3/9999/444/0/9999/2/0/666/55/66/33/6/0/66/2/0/3/777/9999/33/9/444/33')
    print(result)
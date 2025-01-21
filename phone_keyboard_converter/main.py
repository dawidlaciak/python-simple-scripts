def sms_converter(text):

    text = text.upper()

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

    for letter in text:
        
        if letter == ' ':
            converted_text.append('0')

        for key in converter_dict:
            if letter in converter_dict[key]:
                converted_text.append(str(key) * (converter_dict[key].index(letter) + 1))

    print(converter_dict)
    return '/'.join(converted_text)

if __name__ == '__main__':
    result = sms_converter('pomocy lagun siedzi za oknem na drzewie')
    print(result)
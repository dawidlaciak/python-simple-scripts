def sms_converter():

    converter_dict = {}
    letter_number = ord('A')
    
    for i in range(2, 10):
        if i == 9:
            converter_dict[i] = [chr(letter_number+x) for x in range(4)]
            break
        
        converter_dict[i] = [chr(letter_number+x) for x in range(3)]
        letter_number += 3


    print(converter_dict)

sms_converter()
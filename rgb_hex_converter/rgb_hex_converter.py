def convert_rgb_into_hex(rgb:tuple) -> str:

    hex_color = '#'

    if len(rgb) != 3:
        return 'Incorrect RGB color.'
    
    for hue in rgb:

        if hue < 0 or hue > 255:
            return 'Incorrect RGB color.'
        else:
            hex_color += hex(hue).upper()[2:]
    
    return hex_color

print(convert_rgb_into_hex((256, 114, 76)))


def convert_hex_into_rgb(hex_color:str) -> str:

    rgb = []

    if len(hex_color) not in [6, 7]:
        return 'Incorrect HEX color.'
    
    if hex_color[0] == '#':
        hex_color = hex_color[1:]
    
    for i in range(0, len(hex_color) - 1, 2):

        if ord(hex_color[i]) > 70 or ord(hex_color[i]) < 48:
            return 'Incorrect RGB color.'
        else:
            rgb.append(int(hex_color[i] + hex_color[i+1], 16))
        
    return rgb

print(convert_hex_into_rgb(convert_rgb_into_hex((106, 114, 76))))
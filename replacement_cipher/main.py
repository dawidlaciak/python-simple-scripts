def encrypt(packet, key):
    text = packet + ' ' * (key**2 - len(packet)) 
    encrypted_packet = ''
    
    for column in range(key):
        for row in range(key):
            encrypted_packet += text[row * key + column]  
    
    return encrypted_packet


message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et.'
key = 5

start_packet = 0
encrypted_message = ''

while start_packet < len(message):
    packet = message[start_packet : start_packet + key**2]
    start_packet += key**2
    encrypted_message += encrypt(packet, key)

print("Encrypted message:", encrypted_message)

start_packet = 0
decrypted_message = ''

while start_packet < len(encrypted_message):
    packet = encrypted_message[start_packet : start_packet + key**2]
    start_packet += key**2
    decrypted_message += encrypt(packet, key)

print("Decrypted message:", decrypted_message)

number = 5
text = "Hello World"
print(text)
print(text[6])
print(text[-1])
print(len(text))
print(type(text))

shift = 3
print(shift)
print(type(shift))

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.find('z')
index = alphabet.find(text[0].lower())
print(index)
print(text.lower())
shifted = alphabet[index]
print(shifted)
shifted = alphabet[index + shift]
print(shifted)

encrypted_text = ""

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]

print('plain text:', text)
print('encrypted text:', encrypted_text)

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
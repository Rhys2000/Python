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
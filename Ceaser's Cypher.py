text = input("What's the text? ")
shift = input("How much we shifiting by? ")
print("What do you want to do with the text?\n1. Encrypt\n2. Decrypt")
decision = input("Enter the number of your choice: ")
shift = int(shift)
decision = int(decision)

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    text = text.lower()
    text = list(text)
    for i in range(len(text)):
        if text[i] in Alphabet:
            text[i] = Alphabet[(Alphabet.index(text[i]) + shift) % 26]
    print(''.join(text))
    
def decrypt(text, shift):
    text = text.lower()
    text = list(text)
    for i in range(len(text)):
        if text[i] in Alphabet:
            text[i] = Alphabet[(Alphabet.index(text[i]) - shift) % 26]
    print(''.join(text))
    
def ceaser(text, shift, decision):
    text = text.lower()
    text = list(text)
    for i in range(len(text)):
        if text[i] in Alphabet:
            if decision == 1:
                text[i] = Alphabet[(Alphabet.index(text[i]) + shift) % 26]
            elif decision == 2:
                text[i] = Alphabet[(Alphabet.index(text[i]) - shift) % 26]
    print(''.join(text))
    

ceaser(text, shift, decision)

# if shift == '1':
#     encrypt(text, shift)
# elif shift == '2':
#     decrypt(text, shift)
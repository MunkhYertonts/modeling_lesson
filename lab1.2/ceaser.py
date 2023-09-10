# Caesar Cipher 1

import string
MAX_KEY_SIZE = 94
def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def countChr(m):
    all_freq = {}
    for chr in m:
        for i in chr:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    return str(all_freq)

def getMessage():
    print('Enter your message:')
    return input()
    
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
    
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if (ord(symbol)>= 33 and ord(symbol)<=126):
            num = ord(symbol)
            num += key
    
            if symbol.isupper():
                if num > ord('~'):
                    num -= 94
                elif num < ord('!'):
                    num += 94
            elif symbol.islower():
                if num > ord('~'):
                    num -= 94
                elif num < ord('!'):
                    num += 94
            elif symbol.isdigit():
                if num > ord('~'):
                    num -= 94
                elif num < ord('!'):
                    num += 94
            elif ((ord(symbol)>= 33 and ord(symbol)<=47) or 
                  (ord(symbol)>= 58 and ord(symbol)<=64) or 
                  (ord(symbol)>= 91 and ord(symbol)<=96) or 
                  (ord(symbol)>=123 and ord(symbol)<=126)):
                if num > ord('~'):
                    num -= 94
                elif num < ord('!'):
                    num += 94

    
            translated += chr(num)
        else:
            translated += symbol
    return translated   

# mode = getMode()
# message = getMessage()
# key = getKey()

# print('Your translated text is:')
# print(getTranslatedMessage(mode, message, key))

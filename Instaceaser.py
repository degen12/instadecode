# a program that intantly does the ceaser cypher
#origin= input("code: ")
#alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 # Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():
 while True:
     print('Do you wish to encrypt or decrypt a message?')
     mode = input().lower()
     if mode in 'encrypt e decrypt d'.split():
         return mode
     else:
         print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
 print('Enter your message:')
 return input()

#def getKey():
 #key = 0
 #while True:
  #   print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
   #  key = int(input())
    # if (key >= 1 and key <= MAX_KEY_SIZE):
     #    return key

def getTranslatedMessage(mode, message, key):
 if mode[0] == 'd':
     key = -key
 translated = ''

 for symbol in message:
     if symbol.isalpha():
         num = ord(symbol)
         num += key

         if symbol.isupper():
             if num > ord('Z'):
                 num -= 26
             elif num < ord('A'):
                 num += 26
         elif symbol.islower():
             if num > ord('z'):
                 num -= 26
             elif num < ord('a'):
               num += 26



         translated += chr(num)

     else:

         translated += symbol

 return translated
def checkword(file):
    for line in f:
        if getTranslatedMessage(mode,message,key) == line

message = getMessage()
mode = getMode()
f= open('/usr/share/dict/words')
for i in range(26):
    key = i 
    print('Your translated text is:')
    #print(getTranslatedMessage(mode,message,key))
    checkword(f)


        

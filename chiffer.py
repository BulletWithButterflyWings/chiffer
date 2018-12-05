word = "test" #
key = 12 #
letters = [] #
crypt = [] #

for letter in word: # En loop, tills hela ordet är klart. 
    letters.append(ord(letter) + key) #
    
    print(letters) #

for l in letters: #
    crypt.append(chr(l -key)) #

print(crypt)
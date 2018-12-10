word = "" #
key = 12 #
letters = [] #
crypt = [] #
choice = 0

while choice != 3:

    print("Hej och välkomen till krypteringsprogrammet!")
    print("Tryck 1 för kryptering.")
    print("Tryck 2 för dekryptering.")
    print("Tryck 3 för att avsluta.")

    try:
        choice = int(input("Gör ett val:"))
    except:
        print("Du gjorde inte ett val, försök igen.")

    
    if choice == 1:
        word = input("skriv det du vill kryptera: ")
        for letter in word: # En loop, tills hela ordet är klart. 
            letters.append(ord(letter) + key) #
    
        print(letters) #
        

    elif choice == 2:
        word = input("Skriv det du vill dekryptera: ")
        for l in letters: #
            crypt.append(chr(l -key)) #

        print(crypt)
    
    else:
        print("")
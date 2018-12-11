word = "" # 
key = 12 # "Nykeln" till krypteringen är 12.
letters = [] #
crypt = [] #
choice = 0 # Ger "choice" värdet 0.

while choice != 3: # Om du väljer "3" avslutas programmet. 

    print("Hej och välkomen till krypteringsprogrammet!") # Skriver ut värden som har angets.
    print("Tryck 1 för kryptering.")
    print("Tryck 2 för dekryptering.")
    print("Tryck 3 för att avsluta.")
    print("Tryck 4 för att göra mer kryptering.")

    try: #
        choice = int(input("Gör ett val:")) #
    except: #
        print("Du gjorde inte ett val, försök igen.") #

    
    if choice == 1: # Om val "1" väljs, kommer programmet köra detta kommando.
        word = input("Skriv det du vill kryptera: ") #
        for letter in word: # En loop, tills hela ordet är klart. 
            letters.append(ord(letter) + key) #
        for l in letters : #
            print(chr(l)) #
    
        print(letters) #
        

    elif choice == 2: # Om "2" väljs så kommer kommandot nedan att köras.
        word = input("Skriv det du vill dekryptera: ") #
        for l in letters: #
            crypt.append(chr(l -key)) #

        print(crypt) #
    elif choice == 4: #
        word = input("Skriv in din krypterade kod: ") # 
        for l in word: #
            variabel = ord(l) - key #
            print(variabel) #
        
            print(chr(variabel)) # Gör om ett heltal till ett ord.


    else: #
        print("") #
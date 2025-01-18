alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("!--------------------------------------------------------------------------------!")
print("!                       Caesar Cipher app Made By I9MM                           !")
print("!--------------------------------------------------------------------------------!")
while True :
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()
    letter = ""
    if choice == "encode" :
        msg = input("Enter your msg : ").lower()
        num = int(input("Type the shift number : "))
        for char in msg :
            if char in alpha:
                counter_index = alpha.index(char)
                f_index = int(counter_index + num) %len(alpha)
                letter += alpha[f_index]
        print(letter)
        end = input("Type 'yes' if you want to go again. Otherwise type 'no'. : ").lower()
    elif choice == "decode":
        msg = input("Enter your msg : ").lower()
        num = int(input("Type the shift number : "))
        for char in msg :
            if char in alpha :
                counter_index = alpha.index(char)
                f_index = int(counter_index - num) % len(alpha)
                letter += alpha[f_index]
        print(letter)
        end = input("Type 'yes' if you want to go again. Otherwise type 'no'. : ").lower()
    else :
        print ("Enter encode - decode only !! ")
    if end == "yes" :
        letter = ""
        continue
    elif end == "no" :
        print("Goodbye :]")
        break
    else :
        print("Hmm i think you like to try agian ;]")
        print("!!!! Next time plz enter yes or no only !!!!")
        continue

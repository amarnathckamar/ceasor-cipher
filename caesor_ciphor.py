from ntpath import join
import time
import sys
import os

lis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9","@","#","$","%","&","?"]


type_delay = 0.05
delete_delay = 0.01

# function to encrypt data
def encrypt(lis, w, k):
    en = []
    k = int(k)
    length = len(w)
    w = w.lower()
    ind = 0
    for i in range(0, length):
        for j in range(0, 42):
            if (w[i] == lis[j]):
                ind = j+k
                if (ind >= 42):
                    ind = ind-42
                    en.insert(i, lis[ind].upper())
                    ind = 0
                    break
                else:
                    en.insert(i, lis[ind].upper())
                    ind = 0
    time.sleep(1)
    print(" ".join(en))
    return en


# function to decrypt data
def decrypt(lis, w, k):
    en = []
    k = int(k)
    length = len(w)
    w = w.lower()
    ind = 0
    for i in range(0, length):
        for j in range(0, 42):
            if (w[i] == lis[j]):
                ind = j-k
                if (ind < 0):
                    ind = ind+42
                    en.insert(i, lis[ind].upper())
                    ind = 0
                    break
                else:
                    en.insert(i, lis[ind].upper())
                    ind = 0
    time.sleep(1)
    print(" ".join(en))
    return en
    
        

    
def re_pro(lis,en,k,fun):
    typewriter_effect("HOW MANY TIMES:",type_delay,delete_delay)
    limit=eval(input())
    os.system('cls')
    for i in range(0,limit):
    # convert list element to string
        w = ""
        for i in en:
            w += i
        en=fun(lis,w,k)
   

def typewriter_effect(sentence, type_delay, delete_delay):
    # Loop through each character in the sentence
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

    # Pause after printing the entire sentence
    time.sleep(1)

os.system('cls')
# Driver program
if __name__ == '__main__':
    

    # Your desired code continues from here
    print('\n')
    typewriter_effect("ENCRYPT AND DECRYPT",type_delay,delete_delay)
    print("\n")
    typewriter_effect("ENTER ELEMENT WITHOUT SPACE:",type_delay,delete_delay)
    w = input()
    os.system('cls')
    typewriter_effect("ENCRYPT AND DECRYPT",type_delay,delete_delay)
    print("\n")
    typewriter_effect("ENTER THE KEY:",type_delay,delete_delay)
    k = input()

    os.system('cls')

    y = 'y'
    while (y == 'y'):
        typewriter_effect("choose ENCRYPT (e) / DECRYPT (d) :",type_delay,delete_delay)
        choice = input()
        print("\n")
        if choice == 'e':
            en=encrypt(lis, w, k)
            typewriter_effect("repeat? (y/n):",type_delay,delete_delay)
            re=input()
            os.system('cls')
            if re=='y':
                re_pro(lis,en,k,encrypt)
            else:
                continue
        elif choice == 'd':
            en=decrypt(lis, w, k)
            typewriter_effect("repeat? (y/n):",type_delay,delete_delay)
            re=input()
            os.system('cls')
            if re=='y':
                re_pro(lis,en,k,decrypt)
            else:
                continue

        else:
            print("Wrong choice")
        
        print('\n')
        typewriter_effect("Do you want to continue (y/n) :",type_delay,delete_delay)
        y = input()

import time
import sys
import os

# Character list
lis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
       "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "#", "$", "%", "&", "?"]

type_delay = 0.05
delete_delay = 0.01

# Function to encrypt data
def encrypt(lis, w, k):
    en = []
    k = int(k)
    w = w.lower()

    for char in w:
        if char in lis:
            ind = (lis.index(char) + k) % len(lis)
            en.append(lis[ind].upper())
        else:
            en.append(char)  # Keep character as is if not in the list

    time.sleep(1)
    print(" ".join(en))
    return en

# Function to decrypt data
def decrypt(lis, w, k):
    de = []
    k = int(k)
    w = w.lower()

    for char in w:
        if char in lis:
            ind = (lis.index(char) - k) % len(lis)
            de.append(lis[ind].upper())
        else:
            de.append(char)  # Keep character as is if not in the list

    time.sleep(1)
    print(" ".join(de))
    return de

# Function to repeat encryption/decryption process
def re_pro(lis, en, k, fun):
    typewriter_effect("HOW MANY TIMES:", type_delay, delete_delay)
    limit = int(input())
    os.system('cls')

    for _ in range(limit):
        # Convert list element to string
        w = "".join(en)
        en = fun(lis, w, k)

# Function for typewriter effect
def typewriter_effect(sentence, type_delay, delete_delay):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)
    time.sleep(1)

# Clear screen and main driver function
def main():
    os.system('cls')
    print('\n')
    typewriter_effect("ENCRYPT AND DECRYPT", type_delay, delete_delay)
    print("\n")
    typewriter_effect("ENTER ELEMENT WITHOUT SPACE:", type_delay, delete_delay)
    w = input().strip()

    if not all(char in lis for char in w.lower()):
        print("Invalid input. Please enter only valid characters.")
        return

    os.system('cls')
    typewriter_effect("ENCRYPT AND DECRYPT", type_delay, delete_delay)
    print("\n")
    typewriter_effect("ENTER THE KEY:", type_delay, delete_delay)
    k = input().strip()

    if not k.isdigit():
        print("Invalid key. Please enter a number.")
        return

    os.system('cls')

    y = 'y'
    while y.lower() == 'y':
        typewriter_effect("choose ENCRYPT (e) / DECRYPT (d) :", type_delay, delete_delay)
        choice = input().strip().lower()

        if choice == 'e':
            en = encrypt(lis, w, k)
            typewriter_effect("repeat? (y/n):", type_delay, delete_delay)
            if input().strip().lower() == 'y':
                re_pro(lis, en, k, encrypt)

        elif choice == 'd':
            en = decrypt(lis, w, k)
            typewriter_effect("repeat? (y/n):", type_delay, delete_delay)
            if input().strip().lower() == 'y':
                re_pro(lis, en, k, decrypt)

        else:
            print("Wrong choice")

        print('\n')
        typewriter_effect("Do you want to continue (y/n):", type_delay, delete_delay)
        y = input().strip().lower()

if __name__ == '__main__':
    main()

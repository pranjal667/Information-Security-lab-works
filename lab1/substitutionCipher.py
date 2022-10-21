# Python program to demonstrate Substitution Cipher

import string

# A list containing all characters
all_letters = string.ascii_letters

""" 
create a dictionary to store the substitution for the given
alphabet in the plain text based on the key
"""

dictionary1 = {}
key = 6     # enter the key for substitution of respective letters

for i in range(len(all_letters)):
    dictionary1[all_letters[i]] = all_letters[(i+key) % len(all_letters)]

print("Enter the text to be ciphered:")
plain_txt = input()
cipher_txt = []

# loop to generate ciphertext

for char in plain_txt:
    if char in all_letters:
        temp = dictionary1[char]
        cipher_txt.append(temp)
    else:
        temp = char
        cipher_txt.append(temp)

cipher_txt = "".join(cipher_txt)
print("Cipher Text is: ", cipher_txt)


""" 
create a dictionary to store the substitution for the given
alphabet in the cipher  text based on the key
"""


dictionary2 = {}
for i in range(len(all_letters)):
    dictionary2[all_letters[i]] = all_letters[(i-key) % (len(all_letters))]

# loop to recover plain text
decrypt_txt = []

for char in cipher_txt:
    if char in all_letters:
        temp = dictionary2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)
print("Recovered plain text :", decrypt_txt)

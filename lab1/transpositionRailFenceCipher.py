# Python program to demonstrate Rail-Fence Cipher[TRANPOSITION CYPHER]

class railfence:

    def __init__(self, depth):
        self.depth = depth

    def railing(self, text, process):
        plain_text = ""
        rail = [""] * self.depth
        row_counter = [0] * self.depth
        count, row = 0, 0
        for c in "".join(text):
            if (process == 1):
                rail[row] += c
            else:
                rail = text
                plain_text = plain_text + rail[row][row_counter[row]]
                row_counter[row] += 1
            if (count > (2*self.depth-4)):
                count, row = 0, 0
            else:
                count += 1
                row = (row + 1) if (row < self.depth-1) else (row - 1)
        return rail if (process == 1) else plain_text

    def encrypt(self, plain_text):
        rail = self.railing(plain_text, 1)
        cipher_text = "".join(rail)
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ""
        rail = self.railing(cipher_text, 1)
        l = 0
        for i in range(self.depth):
            rail[i] = cipher_text[l:l+len(rail[i])]
            l = l + len(rail[i])
        plain_text = self.railing(rail, 2)
        return plain_text


depth = int(input("Enter the depth: "))
rf = railfence(depth)

plain_text = input("Enter the plain text: ")

cipher_text = rf.encrypt(plain_text)
print("Encrypted text: " + cipher_text.upper())

print('Do you want to decrypt the encrypted text? Enter Y or N:')
decision = input()
if decision == 'Y' or decision == 'y':
    plain_text = rf.decrypt(cipher_text)
    print("Decrypted text: " + plain_text.upper())
else:
    print("")

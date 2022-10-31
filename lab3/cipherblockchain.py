from des import DesKey

key = DesKey(b"some key")
encrypted_message = []
decrypted_message = []


def des_encrypt(message):
    for i in message:
        encrypted_message.append(key.encrypt(i, padding=True))
    return encrypted_message


def des_decrypt(message):
    for i in message:
        decrypted_message.append(key.decrypt(i, padding=True))
    return decrypted_message


messages = [b"I am student of Kathmandu University", b"Final Year"]
des_encrypt(messages)

print(encrypted_message)

des_decrypt(encrypted_message)

print(decrypted_message)

encrypted_message = []
decrypted_message = []


class CipherBlockChain:
    def __init__(self, message):
        self.message = message

    def des_encrypt(self, message):
        for i in self.message:
            encrypted_message.append(key.encrypt(i, padding=True))
        return encrypted_message

    def des_decrypt(self, message):
        for i in message:
            decrypted_message.append(key.decrypt(i, padding=True))
        return decrypted_message


text = CipherBlockChain([b"My name is Pranjal Ghimire"])

print(text.message)

en = text.des_encrypt(text.message)
print(en)

print(text.des_decrypt(en))

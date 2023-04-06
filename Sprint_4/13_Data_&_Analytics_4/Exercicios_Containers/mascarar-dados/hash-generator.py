import hashlib

while True:
    string = input("Digite uma string: ")

    hash_object = hashlib.sha1(string.encode())

    print("Hash SHA-1 da string: ", hash_object.hexdigest())

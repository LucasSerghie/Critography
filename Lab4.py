import random
from sympy import mod_inverse

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
P = 29

def generate_keys():
    """
    Generates public and private keys for the ElGamal encryption scheme.
    """
    private_key = random.randint(2, P - 2)

    g = random.randint(2, P - 1)
    h = pow(g, private_key, P)

    return (g, h), private_key

def encrypt(public_key, plaintext):
    """
    Encrypts a plaintext message using the ElGamal encryption scheme.

    Parameters:
    - public_key (tuple): Public key (g, h) for encryption.
    - plaintext (str): The plaintext message to be encrypted.

    Returns:
    - tuple: A tuple containing the first part of the ciphertext (c1) and a list of encrypted characters (c2).
    """
    g, h = public_key
    k = random.randint(2, P - 2)
    c1 = pow(g, k, P)

    encrypted_text = []
    for char in plaintext:
        m = ALPHABET.index(char.upper())
        c2 = (m * pow(h, k, P)) % P
        encrypted_text.append(c2)

    return c1, encrypted_text

def decrypt(private_key, ciphertext):
    """
    Decrypts a ciphertext message using the ElGamal decryption scheme.

    Parameters:
    - private_key (int): Private key for decryption.
    - ciphertext (tuple): A tuple containing the first part of the ciphertext (c1) and a list of encrypted characters (c2).

    Returns:
    - str: The decrypted plaintext message.
    """
    c1, encrypted_text = ciphertext
    decrypted_text = ""

    for c2 in encrypted_text:
        s = pow(c1, private_key, P)
        m = (c2 * mod_inverse(s, P)) % P
        decrypted_text += ALPHABET[m]

    return decrypted_text

public_key, private_key = generate_keys()
plaintext = "HELLO"
ciphertext = encrypt(public_key, plaintext)
decrypted_text = decrypt(private_key, ciphertext)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
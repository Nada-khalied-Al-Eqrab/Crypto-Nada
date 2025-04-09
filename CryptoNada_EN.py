import string
import random
# import numpy as np
1
# -------------------- General Tools --------------------
ALPHABET = string.ascii_letters + string.digits + string.punctuation + ' '

# -------------------- 1. Additive Cipher --------------------
def additive_encrypt(text, key):
    return ''.join(chr((ord(char) + key) % 256) for char in text)

def additive_decrypt(text, key):
    return ''.join(chr((ord(char) - key) % 256) for char in text)

# -------------------- 2. Multiplicative Cipher --------------------
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse for the key")

def multiplicative_encrypt(text, key):
    return ''.join(chr((ord(char) * key) % 256) for char in text)

def multiplicative_decrypt(text, key):
    inv = modinv(key, 256)
    return ''.join(chr((ord(char) * inv) % 256) for char in text)

# -------------------- 3. Affine Cipher --------------------
def affine_encrypt(text, a, b):
    return ''.join(chr((ord(char) * a + b) % 256) for char in text)

def affine_decrypt(text, a, b):
    inv = modinv(a, 256)
    return ''.join(chr(((ord(char) - b) * inv) % 256) for char in text)

# -------------------- 4. Monoalphabetic Substitution Cipher --------------------
def mono_substitution_encrypt(text, key_map):
    return ''.join(key_map.get(char, char) for char in text)

def mono_substitution_decrypt(text, key_map):
    return ''.join(key_map.get(char, char) for char in text)

# -------------------- 5. Vigenere Cipher --------------------
def vigenere_encrypt(text, key):
    key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(chr((ord(t) + ord(k)) % 256) for t, k in zip(text, key))

def vigenere_decrypt(text, key):
    key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(chr((ord(t) - ord(k)) % 256) for t, k in zip(text, key))

# -------------------- 6. Autokey Cipher --------------------
def autokey_encrypt(text, key):
    key += text
    key = key[:len(text)]
    return ''.join(chr((ord(t) + ord(k)) % 256) for t, k in zip(text, key))

def autokey_decrypt(text, key):
    result = ''
    for i in range(len(text)):
        k = key[i] if i < len(key) else result[i - len(key)]
        result += chr((ord(text[i]) - ord(k)) % 256)
    return result

# -------------------- 7. Playfair Cipher --------------------
def prepare_playfair_matrix(key):
    matrix = []
    seen = set()
    for char in key + ALPHABET:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+8] for i in range(0, 64, 8)]

def playfair_process(text):
    result = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            result.append((a, 'X'))
            i += 1
        else:
            result.append((a, b))
            i += 2
    return result

def playfair_encrypt(text, key):
    matrix = prepare_playfair_matrix(key)
    pairs = playfair_process(text)
    result = ''
    for a, b in pairs:
        row1, col1 = divmod(matrix[0].index(a), 8)
        row2, col2 = divmod(matrix[0].index(b), 8)
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 8] + matrix[row2][(col2 + 1) % 8]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 8][col1] + matrix[(row2 + 1) % 8][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def playfair_decrypt(text, key):
    matrix = prepare_playfair_matrix(key)
    pairs = playfair_process(text)
    result = ''
    for a, b in pairs:
        row1, col1 = divmod(matrix[0].index(a), 8)
        row2, col2 = divmod(matrix[0].index(b), 8)
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 8] + matrix[row2][(col2 - 1) % 8]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 8][col1] + matrix[(row2 - 1) % 8][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

# -------------------- 8. Hill Cipher --------------------
def hill_encrypt(text, key_matrix):
    n = len(key_matrix)
    while len(text) % n != 0:
        text += ' '
    result = ''
    for i in range(0, len(text), n):
        vector = np.array([ord(c) for c in text[i:i+n]])
        res = np.dot(key_matrix, vector) % 256
        result += ''.join(chr(x) for x in res)
    return result

def hill_decrypt(text, key_matrix):
    det = int(round(np.linalg.det(key_matrix)))
    inv_det = modinv(det % 256, 256)
    adjugate = np.round(np.linalg.inv(key_matrix) * det).astype(int)
    inverse_matrix = (inv_det * adjugate) % 256
    return hill_encrypt(text, inverse_matrix)

# -------------------- 9. One-Time Pad Cipher --------------------
def otp_encrypt(text, key):
    return ''.join(chr((ord(t) ^ ord(k)) % 256) for t, k in zip(text, key))

def otp_decrypt(text, key):
    return otp_encrypt(text, key)

# -------------------- 10. Rotor Cipher --------------------
def rotor_encrypt(text, rotor):
    return ''.join(chr((ord(c) + rotor[i % len(rotor)]) % 256) for i, c in enumerate(text))

def rotor_decrypt(text, rotor):
    return ''.join(chr((ord(c) - rotor[i % len(rotor)]) % 256) for i, c in enumerate(text))

# -------------------- 11. Enigma Cipher --------------------
def enigma_encrypt(text, rotor1, rotor2):
    return ''.join(chr((ord(c) + rotor1[i % len(rotor1)] + rotor2[i % len(rotor2)]) % 256) for i, c in enumerate(text))

def enigma_decrypt(text, rotor1, rotor2):
    return ''.join(chr((ord(c) - rotor2[i % len(rotor2)] - rotor1[i % len(rotor1)]) % 256) for i, c in enumerate(text))

# -------------------- 12. Keyless Transposition --------------------
def keyless_transposition_encrypt(text):
    return text[::-1]

def keyless_transposition_decrypt(text):
    return text[::-1]

# -------------------- 13. Keyed Transposition --------------------
def keyed_transposition_encrypt(text, key):
    order = sorted(range(len(key)), key=lambda k: key[k])
    rows = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
    result = ''
    for row in rows:
        row += ' ' * (len(key) - len(row))
        result += ''.join(row[i] for i in order)
    return result

def keyed_transposition_decrypt(text, key):
    order = sorted(range(len(key)), key=lambda k: key[k])
    inverse_order = sorted(range(len(order)), key=lambda k: order[k])
    rows = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
    result = ''
    for row in rows:
        row += ' ' * (len(key) - len(row))
        result += ''.join(row[i] for i in inverse_order)
    return result

# -------------------- 14. Combined Transposition --------------------
def combined_transposition_encrypt(text, key):
    return keyed_transposition_encrypt(keyless_transposition_encrypt(text), key)

def combined_transposition_decrypt(text, key):
    return keyless_transposition_decrypt(keyed_transposition_decrypt(text, key))

# -------------------- 15. Interactive Menu --------------------
def main():
    print("\nNada's Crypto Program for Encryption Algorithms\n")
    print("Choose an operation:")
    print("1. Encrypt")
    print("2. Decrypt")
    mode = input("Enter operation number: ")

    print("\nChoose encryption method:")
    options = {
        1: "Additive Cipher",
        2: "Multiplicative Cipher",
        3: "Affine Cipher",
        4: "Monoalphabetic Substitution Cipher",
        5: "Vigenere Cipher",
        6: "Autokey Cipher",
        7: "Playfair Cipher",
        8: "Hill Cipher",
        9: "One-Time Pad Cipher",
        10: "Rotor Cipher",
        11: "Enigma Cipher",
        12: "Keyless Transposition",
        13: "Keyed Transposition",
        14: "Combined Transposition"
    }
    for i in range(1, 15):
        print(f"{i}. {options[i]}")

    cipher_choice = int(input("\nEnter encryption type number: "))
    text = input("\nEnter the text: ")

    result = ""
    if cipher_choice == 1:
        key = int(input("Enter the numeric key: "))
        result = additive_encrypt(text, key) if mode == '1' else additive_decrypt(text, key)
    elif cipher_choice == 2:
        key = int(input("Enter numeric key (must be coprime with 256): "))
        result = multiplicative_encrypt(text, key) if mode == '1' else multiplicative_decrypt(text, key)
    elif cipher_choice == 3:
        a = int(input("Enter coefficient a: "))
        b = int(input("Enter coefficient b: "))
        result = affine_encrypt(text, a, b) if mode == '1' else affine_decrypt(text, a, b)
    elif cipher_choice == 4:
        shuffled = list(ALPHABET)
        random.shuffle(shuffled)
        key_map = dict(zip(ALPHABET, shuffled))
        if mode == '2':
            key_map = dict(zip(shuffled, ALPHABET))
        result = mono_substitution_encrypt(text, key_map) if mode == '1' else mono_substitution_decrypt(text, key_map)
    elif cipher_choice == 5:
        key = input("Enter the keyword: ")
        result = vigenere_encrypt(text, key) if mode == '1' else vigenere_decrypt(text, key)
    elif cipher_choice == 6:
        key = input("Enter the keyword: ")
        result = autokey_encrypt(text, key) if mode == '1' else autokey_decrypt(text, key)
    elif cipher_choice == 7:
        key = input("Enter the keyword: ")
        result = playfair_encrypt(text, key) if mode == '1' else playfair_decrypt(text, key)
    elif cipher_choice == 8:
        print("Example of a key matrix: [[3,3],[2,5]]")
        matrix = eval(input("Enter a 2x2 or 3x3 key matrix as Python list: "))
        result = hill_encrypt(text, np.array(matrix)) if mode == '1' else hill_decrypt(text, np.array(matrix))
    elif cipher_choice == 9:
        key = input("Enter a key of same length as the text: ")
        result = otp_encrypt(text, key) if mode == '1' else otp_decrypt(text, key)
    elif cipher_choice == 10:
        rotor = list(map(int, input("Enter rotor numbers separated by space: ").split()))
        result = rotor_encrypt(text, rotor) if mode == '1' else rotor_decrypt(text, rotor)
    elif cipher_choice == 11:
        rotor1 = list(map(int, input("Enter first rotor: ").split()))
        rotor2 = list(map(int, input("Enter second rotor: ").split()))
        result = enigma_encrypt(text, rotor1, rotor2) if mode == '1' else enigma_decrypt(text, rotor1, rotor2)
    elif cipher_choice == 12:
        result = keyless_transposition_encrypt(text) if mode == '1' else keyless_transposition_decrypt(text)
    elif cipher_choice == 13:
        key = input("Enter keyword (e.g., ZEBRAS): ")
        result = keyed_transposition_encrypt(text, key) if mode == '1' else keyed_transposition_decrypt(text, key)
    elif cipher_choice == 14:
        key = input("Enter keyword: ")
        result = combined_transposition_encrypt(text, key) if mode == '1' else combined_transposition_decrypt(text, key)
    else:
        print("Invalid option")

    print("\nResult:", result)

if __name__ == "__main__":
    main()

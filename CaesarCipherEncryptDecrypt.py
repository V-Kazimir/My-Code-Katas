#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string


def caesar_cipher(text, shift, encrypt=True):
    """
Caesar Cipher Cryptography Tool

This program is a Caesar cipher encryption and decryption tool that takes user input for the 
text to be encrypted/decrypted, the shift value, and whether the text should be encrypted or decrypted.

    """
    # Create a placeholder list
    result = list(range(len(text)))

    alphabet = string.ascii_lowercase

    # Create shifted alphabet
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):
        # Check for spaces or punctuation
        if letter not in alphabet:
            result[i] = letter
            continue

        # Find the original index position
        original_index = alphabet.index(letter)

        if encrypt:
            # Shifted letter for encryption
            new_letter = shifted_alphabet[original_index]
        else:
            # Shifted letter for decryption
            new_letter = alphabet[(original_index - shift) % 26]

        result[i] = new_letter

    return ''.join(result)


# Prompt user for input and call the function
text = input("Enter text to encrypt/decrypt: ")
shift = int(input("Enter shift value: "))
encrypt = input("Encrypt or decrypt? (e/d): ")

if encrypt.lower() == "e":
    encrypted_text = caesar_cipher(text, shift, encrypt=True)
    print("Encrypted text:", encrypted_text)
elif encrypt.lower() == "d":
    decrypted_text = caesar_cipher(text, shift, encrypt=False)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid option.")


# In[ ]:





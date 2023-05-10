{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "    Caesar Cipher Encrypter/Decrypter\n",
    "    This program allows the user to either encrypt or decrypt a given text using the Caesar cipher. \n",
    "    The user is prompted to enter the text to be processed, as well as the shift value to be used for the cipher..\n",
    "    \n",
    "'''\n",
    "\n",
    "import string\n",
    "\n",
    "def encrypt(text, shift):\n",
    "  \n",
    "\n",
    "    # Create a placeholder list\n",
    "    encrypted_text = list(range(len(text)))\n",
    "\n",
    "    alphabet = string.ascii_lowercase\n",
    "\n",
    "    # Create shifted alphabet\n",
    "    first_half = alphabet[:shift]\n",
    "    second_half = alphabet[shift:]\n",
    "    shifted_alphabet = second_half+first_half\n",
    "\n",
    "    for i,letter in enumerate(text.lower()):\n",
    "\n",
    "        # Check for spaces or punctuation\n",
    "        if letter in alphabet:\n",
    "            # Find the original index position\n",
    "            original_index = alphabet.index(letter)\n",
    "\n",
    "            # Shifted letter\n",
    "            new_letter = shifted_alphabet[original_index]\n",
    "\n",
    "            encrypted_text[i] = new_letter\n",
    "\n",
    "        # Punctuation or space\n",
    "        else:\n",
    "            encrypted_text[i] = letter\n",
    "\n",
    "    return ''.join(encrypted_text)\n",
    "\n",
    "# Prompt user for input and call the function\n",
    "text = input(\"Enter text to encrypt: \")\n",
    "shift = int(input(\"Enter shift value: \"))\n",
    "encrypted_text = encrypt(text, shift)\n",
    "print(\"Encrypted text:\", encrypted_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

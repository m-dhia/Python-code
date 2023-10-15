# Import necessary libraries
import random
import string

# Define the character set for encryption (punctuation, digits, letters, and space)
chars = string.punctuation + string.digits + string.ascii_letters + " "

# Convert the character set to a list for shuffling
chars = list(chars)

# Create a copy of the character set to use as the key
key = chars.copy()

# Shuffle the key to create a mapping for encryption
random.shuffle(key)

# User input to enter a message for encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# Encrypt the entered message using the shuffled key
for letter in plain_text:
    index = chars.index(letter)  # Find the index of the current character in the original character set
    cipher_text += key[index]    # Use the index to find the corresponding character in the key

# Print the original and encrypted messages
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# User input to enter a message for decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

# Decrypt the entered message using the key
for letter in cipher_text:
    index = key.index(letter)  # Find the index of the current character in the key
    plain_text += chars[index]  # Use the index to find the corresponding character in the original character set

# Print the encrypted message and the decrypted original message
print(f"Encrypted message: {cipher_text}")
print(f"Decrypted original message: {plain_text}")
<h1>Caesar Cipher</h1>
This project implements the Caesar Cipher, a classic encryption technique where each letter in the plaintext is shifted by a fixed number of places down or up the alphabet. Additionally, this implementation has been extended to handle special characters, allowing for a more comprehensive encryption and decryption process.

<h2>Overview</h2>
The Caesar Cipher is a type of substitution cipher in which each letter of the message is replaced by a letter some fixed number of positions down the alphabet. This script provides two functions: one for encrypting a message and another for decrypting it.

<h2>Encryption</h2>
How It Works
<h3>Initialization</h3>: The encryption function starts by initializing an empty string to hold the encrypted message.
<h3>Processing Each Character:</h3>
<h4>Alphabetic Characters:</h4>
For uppercase letters, the ASCII value of 'A' (65) is used as a base.
For lowercase letters, the ASCII value of 'a' (97) is used as a base.
Each letter is shifted by a specified number of positions. The shift wraps around if it goes past 'Z' or 'z', ensuring that it stays within the alphabet.
<h4>Non-Alphabetic Characters:</h4>
Spaces are preserved as they are.
Other non-alphabetic characters are processed based on their ASCII values. The script handles different ranges of non-alphabetic characters separately to ensure they are correctly shifted or left unchanged.
<h3>Building the Encrypted Message:</h3> Each processed character is appended to the encrypted message string.
<h2>Decryption</h2>
How It Works
<h3>Initialization:</h3> The decryption function starts similarly, with an empty string to store the decrypted message.
<h3>Processing Each Character:</h3>
<h4>Alphabetic Characters:</h4>
The base ASCII value is determined based on whether the letter is uppercase or lowercase.
The letter is shifted in the opposite direction of encryption to retrieve the original character. The shift wraps around if it goes before 'A' or 'a'.
<h4>Non-Alphabetic Characters:</h4>
Spaces remain unchanged.
Other non-alphabetic characters are adjusted based on their ASCII ranges, ensuring they are processed correctly.
<h3>Building the Decrypted Message:</h3> Each processed character is appended to the decrypted message string.
<h2>Usage</h2>
<h3>Input:</h3> You provide a message and a shift value when prompted.
<h3>Output:</h3> The script outputs both the encrypted and decrypted versions of the message.

#caesar cipher
def encrypt(message,shift):
  encrypted_message='' #initializing the encrypted message
  for i in range(len(message)):
    if message[i].isalpha():#alphabetic characters
      if message[i].isupper():#keeps the upper case
        base=65 #ascii value of A
      if message[i].islower():#keeps the upper case
        base=97 #ascii value of a
      encrypted_letter=chr((ord(message[i])-base+shift)%26+base)#shifting the letter
    else:
      if message[i]==' ': 
        encrypted_letter=' '#keeps the space
      elif 32 <= ord(message[i]) <= 64:#non alphabetic characters
        base=32
        encrypted_letter=chr((ord(message[i])-base+shift)%33+base)
      elif 91 <= ord(message[i]) <= 96:
        base=91
        encrypted_letter=chr((ord(message[i])-base+shift)%6+base)
      elif 123 <= ord(message[i]) <= 126:
        base=123
        encrypted_letter=chr((ord(message[i])-base+shift)%4+base)
      else:
        encrypted_letter=message[i] #non-printable characters remain unchanged
    encrypted_message+=encrypted_letter
  return encrypted_message
def decrypt(message,shift):
  decrypted_message=''#initializing the decrypted message
  for i in range(len(message)):
    if message[i].isalpha():#alphabetic characters
      if message[i].isupper():#keeps the upper case
        base=65
      if message[i].islower():#keeps the lower case
        base=97
      decrypted_letter=chr((ord(message[i])-base-shift)%26+base)
    else:
      if message[i]==' ':#keeps the space
        decrypted_letter=' '
      elif 32 <= ord(message[i]) <= 64:#non alphabetic characters
        base=32
        decrypted_letter=chr((ord(message[i])-base-shift)%33+base)
      elif 91 <= ord(message[i]) <= 96:
        base=91
        decrypted_letter=chr((ord(message[i])-base-shift)%6+base)
      elif 123 <= ord(message[i]) <= 126:
        base=123
        decrypted_letter=chr((ord(message[i])-base-shift)%4+base)
      else:
        decrypted_letter=message[i] #non-printable characters remain unchanged
    decrypted_message+=decrypted_letter
  return decrypted_message

text=input('enter the message you want to encrypt/decrypt: ')#taking the message as input
shift=int(input('enter the shift value: '))#taking the shift value as input
print(f"encrypted text: {encrypt(text,shift)}")#printing the encrypted message
print(f"decrypted text: {decrypt(text,shift)}")#printing the decrypted message
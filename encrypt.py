import string
def encrypt(message, shift):
    alphabet = string.ascii_lowercase
    encrypted_message =""
    for letter in message :
           if letter.lower() in alphabet:
                original_position=alphabet.index(letter.lower())
                new_position = (original_position + shift) % 26
                encrypted_letter=alphabet[new_position]
                #حافظ علي حالة الحرف
                if letter.isupper():
                    encrypted_letter =encrypted_letter.upper()
                encrypted_message+=encrypted_letter
           else:

                encrypted_message += letter
    print(encrypted_message)    
#ناخذ الرسالة و عدد حروف الانتقال
user_message= input("Enter a message : \n")
shift_number =int(input("Enter a shift number:"))
encrypt(message=user_message,shift=shift_number )
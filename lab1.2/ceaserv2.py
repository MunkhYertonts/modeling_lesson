def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
       
            is_upper = char.isupper()
            
  
            char_index = ord(char.lower()) - ord('a')
            
   
            new_index = (char_index + shift) % 26
            
         
            new_char = chr(new_index + ord('a'))
            
        
            if is_upper:
                new_char = new_char.upper()
            
            result += new_char
        else:

            result += char
    
    return result

# # Example usage:
# plaintext = "Hello, World!"
# shift = 3
# encrypted_text = caesar_cipher(plaintext, shift)
# print("Encrypted:", encrypted_text)

# # To decrypt, simply use a negative shift:
# decrypted_text = caesar_cipher(encrypted_text, -shift)
# print("Decrypted:", decrypted_text)
#----------------------------------------------------------------------------------------------------
# def alphabet_frequency(text):

#     frequency_dict = {}

#     # Iterate through each character in the text
#     for char in text:
#         # Check if the character is an alphabetic character (either uppercase or lowercase)
#         if char.isalpha():
#             # Convert the character to lowercase to ensure case insensitivity
#             char = char.lower()

#             # Check if the character is already in the dictionary
#             if char in frequency_dict:
#                 # If it is, increment the count
#                 frequency_dict[char] += 1
#             else:
#                 # If it's not, add it to the dictionary with a count of 1
#                 frequency_dict[char] = 1

#     return frequency_dict

# # Example usage:
# text = "Hhhello, World! 12--""3"
# frequency = alphabet_frequency(text)

# # Print the alphabet character frequencies
# for letter, count in frequency.items():
#     print(f"Letter: {letter}, Frequency: {count}")

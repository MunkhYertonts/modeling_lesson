f = open("lab1.2/plain.txt","r")
f1 = open("lab1.2/encrypted.txt","w")    
from ceaser import * 
from ceaserv2 import *
# print(countChr(f))
mode="e"

key=4

for line in f:
    # print("line: "+line)
    sentence =line.split()
    myline= ""
    for word in sentence:
        # dec=getTranslatedMessage(mode, word, key)
        dec = caesar_cipher(word,key)
        # print(word+": "+dec)
        myline+=dec+" "	
    # print(myline)
    f1.write(myline+"\n")

def alphabet_frequency_from_file(file_path):

    frequency_dict = {}
    total_characters = 0  

    try:
      
        with open(file_path, 'r') as file:
       
            for line in file:
               
                for char in line:
                   
                    if char.isalpha():
                      
                        char = char.lower()

                        if char in frequency_dict:
                     
                            frequency_dict[char] += 1
                        else:
                     
                            frequency_dict[char] = 1
                    total_characters += 1  

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return frequency_dict, total_characters



# def print_frequency_table(frequency_dict):
#     # Print the table header
#     print("Character  Frequency")
#     print("--------------------")

#     # Print each character and its frequency in a formatted way
#     for char, frequency in sorted(frequency_dict.items()):
#         print(f"{char:^9}  {frequency:^9}")

def histogram(frequency_dict):

    max_frequency = max(frequency_dict.values())

   
    bar_character = '■'  
    space_character = ' ' 

  
    for char in sorted(frequency_dict.keys()):
        frequency = frequency_dict[char]
        scaled_frequency = int(100 * frequency / max_frequency)  # Scale 

       
        fancy_bar = bar_character * scaled_frequency + space_character * (100 - scaled_frequency)


        print(f"{char}: {fancy_bar} ({frequency} occurrences)")

def calculate_per_character_probability(frequency_dict, total_characters):
    # Calculate and display the per-character probability
    print("Character  Frequency  Probability")
    print("---------------------------------")
    for char, frequency in sorted(frequency_dict.items()):
        probability = frequency / total_characters
        print(f"{char:^9}  {frequency:^9}  {probability:.4f}")

file_path = 'lab1.2/plain.txt'
result,total_chars = alphabet_frequency_from_file(file_path)
# print(print_frequency_table(result))
histogram(result)
calculate_per_character_probability(result, total_chars)

f.close()
f1.close()



#!/usr/bin/python3

# Challenge 16
# Dylan Dempsey
# 05/08/23
# Brute force attack tool

# Main

import time

def mode1(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)  # Adjust the delay duration as needed

def mode2(input_string, file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    
    if input_string in words:
        print("The input string is present in the word list.")
    else:
        print("The input string is not present in the word list.")

def mode3(input_string, file_path):
    found = False
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            print(word)
            if word == input_string:
                found = True
            time.sleep(1)

    if found:
        print(f"The input string '{input_string}' is present in the word list.")
    else:
        print(f"The input string '{input_string}' is not present in the word list.")

def main():
    print("Select a mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. Combined Mode")
    mode = int(input("Enter the mode number (1, 2, or 3): "))
    
    if mode == 1:
        file_path = input("Enter the word list file path: ")
        mode1(file_path)
    elif mode == 2:
        input_string = input("Enter the input string: ")
        file_path = input("Enter the word list file path: ")
        mode2(input_string, file_path)
    elif mode == 3:
        input_string = input("Enter the input string: ")
        file_path = input("Enter the word list file path: ")
        mode3(input_string, file_path)
    else:
        print("Invalid mode selection. Please enter either 1, 2, or 3.")

if __name__ == "__main__":
    main()
#End

#ChatGPT was referenced for this code.

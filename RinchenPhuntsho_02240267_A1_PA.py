import math
import re
def start():
    while True:
        print("select a function(1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonantsin string")
        print("4. Find minimum and maximum numbers")
        print("5. Check for plaindrome")
        print("6. Word counter")
        print("0. Exit program")
        your_choice = int(input("Enter your choice:"))

        #Coding of prime number sum
        if your_choice==1:
            def prime_number(number):
                if number < 2:
                    return False
                for i in range (2, int(number**0.5)+ 1):
                    if number % i ==0:
                        return False
                    return True
            def sum_prime(start,end):
                return sum( number for number in range(start,end+1)if prime_number(number))
            start = int(input("Enter start of range:"))
            end = int(input("Enter end of range:"))
            print("Sum of prime number's in range:", sum_prime(start,end))

        #Length unit converter
        elif your_choice==2:
            value = float(input("Enter value:"))
            direction = input("Enter direction(M/F):")
            if direction.upper() == "M":
                converted_value = round(value * 3.28084, 2)
            elif direction.upper() == "F":
                converted_value = round(value / 3.28084, 2)
            else:
                converted_value = "Invalid direction"
            print(f"Converted value:{converted_value}")
        
        #Consonant counter
        elif your_choice==3:
            text = input("Enter a text string:")
            count_consonants = lambda text: sum(1 for char in text.lower()if char.isalpha()and char not in "aeiou")
            print("Number of consonants:",count_consonants(text))
        
        #Min-Max number finder
        elif your_choice==4:
            def min_max_finder():
                n = int(input("How many numbers will you enter?"))
                numbers = [float(input(f"Enter number{i+1}:"))for i in range(n)]
                return min(numbers),max(numbers)
            min_value, max_value =min_max_finder()
            print(f"Min: {min_value}, Max:{max_value}")
        
        #Palindrome checker
        elif your_choice==5:
            def palindrome(text):
                cleaned_text = re.sub(r'[^a-zA-Z0-9]', '',text).lower()
                return cleaned_text== cleaned_text[::-1]
            text= input("Enter a text string:")
            print("Palindrome checker:", palindrome(text))
        
        #Word counter
        elif your_choice==6:
            def word_counter(file_path):
                word_list = ["is", "were", "but"]
                try:
                    with open(file_path, "r", encoding = "utf-8")as file:
                        text_content = file.read().lower().split()
                        word_counts = {}
                        for word in word_list:
                            word_counts[word] = text_content.count(word)
                    return word_counts
                except FileNotFoundError:
                    print("Error: The file was not fount.")
            file_path = input("Enter the file_path:")

            print("word count results:", word_counter(file_path))

        elif your_choice==0:
            print("Exiting program. Goodbye!")
            break
    
        else:
            print("invalid option")
start()

        




    

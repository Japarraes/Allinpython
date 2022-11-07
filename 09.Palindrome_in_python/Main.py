from palindrome import *

# Check for a palindrome string using recursion  

def main():
    
    text = str(input("Enter a string: "))
    text_noSpace = "".join(text.split()).lower()

    if (isPalindrome(text_noSpace)):
        print(f"The text {text} is a palindrome.")
    else:
        print(f"The text {text} is NOT a palindrome.")

    
if __name__ == "__main__":
    main()

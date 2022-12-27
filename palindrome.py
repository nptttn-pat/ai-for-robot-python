#This is Palindrome program
while(1):
    word = str(input("String: "))
    if(word==word[::-1]):
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")



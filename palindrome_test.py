import string


a = input("String: ")
if(a == a[::-1]):
    print("This word is a palindrome")
else:
     print("This word is not a palindrome")

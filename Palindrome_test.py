while(1):
    i = input("String: ")
    if i == i[::-1]:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")
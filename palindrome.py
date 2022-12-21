str = input("String: ")

front = -1
back = len(str)

while front <= back :
    front += 1 
    back -= 1
    if str[front] != str[back] :
        print("This word is not palindrome")
        break
    if (front == back) or (front == back + 1) :
        print("This word is palindrome")
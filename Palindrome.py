Text = input("String: ")
Length = len(Text)
if Text == Text[::-1]:
  print("This word is a palindrome")
else :
  print("This word is not a palindrome")
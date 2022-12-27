def is_palindrome(s):
  s = s.lower()
  s = s.replace(' ', '')
  if s == s[::-1]:
    print("This word is a palindrome")
  else:
    print("This word is not a palindrome")
    
string = input('String: ')
is_palindrome(string)
inp = input('Input string: ')
print("Entered: ",inp)
def pali(s):
    return s == s[::-1]
chk = pali(inp)
if chk:
    print("This word is a Palindrome")
else:
    print("This word is not a Palindrome")

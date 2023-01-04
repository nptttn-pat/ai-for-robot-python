def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = input("String:")
ans = isPalindrome(s)

if ans:
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")

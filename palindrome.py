word = list(input('String: '))
start = 0
end = len(word) - 1
while(1):
    if word[start] != word[end]:
        print('This word is not a palindrome')
        break
    if start > len(word)/2:
        print('This word is a palindrome')
        break
    start+=1
    end-=1
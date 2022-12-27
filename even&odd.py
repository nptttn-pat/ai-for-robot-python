#This is odd or even program
def eod (number):
    if(number%2==0):
        print("even")
    else:
        print("odd")
    return;
while(1):
    number = int(input("Input number: "))
    eod(number)
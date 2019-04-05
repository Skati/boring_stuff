def collatz(number):
    while number!=1:
        if number%2==0:
            print(number//2)
            return number//2

        else:
            print(number*3+1)
            return number*3+1
n=10
while n != 1:
    n = collatz(int(n))

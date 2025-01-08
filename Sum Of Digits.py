num = int(input("Enter a number to check..."))
sum = 0
def Sum(n,sum):
    if n<10:
        return n+sum
    return Sum(n//10,n%10+sum)
print(Sum(num,0))
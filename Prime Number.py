num = int(input("Enter the number to Check...."))

def ispr(num):
    for i in range(2,num):
        for j in range(2,11):
            if i*j==num:
                return False
    return True
if num>0:
    print(ispr(num))

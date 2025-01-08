num = int(input("Enter number to Find the Factorial....."))
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
    
print("Factorial Number of ",num,"is :",fact(num))

# 5*5-1
# 5*4*4-1
# 5*4*3*3-1
# 5*4*3*2*2-1
# 5*4*3*2*1=120

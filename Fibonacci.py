lst = [0,1]
num = int(input("Enter the Number to Find the Fibonacci..."))
for i in range(0,num-2):
    lst.append(lst[-1]+lst[-2])
print(lst)
print(','.join(str(j) for j in lst))
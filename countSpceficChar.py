str = input("Enter the string...")
char = input("Enter the Specific Character...")
count=0
for i in str:
    if i == char:
        count +=1
print(count," Number of times Occured in given String. ")
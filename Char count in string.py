string = input("Enter a String...")
temp = {}
for i in string:
    temp.update({i : string.count(i)})
for i,j in temp.items():
    print(i," Occured ",j," Times")
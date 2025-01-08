s = input("enter the string....")
if s.lower() == s[::-1].lower():
    print("True")
else:
    print("False")
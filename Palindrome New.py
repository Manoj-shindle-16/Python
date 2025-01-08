import string

s = input("Enter a string to check...")
#new = ''.join(i for i in s if i.isalnum())
new = ''.join(char.lower() for char in s if char in string.ascii_letters)
if s.lower() == new[::-1].lower():
    print("The word is pure")
elif new.lower() == new[::-1].lower():
    print("The pharase holds symmetry")
else:
    print("the word lacks balance")
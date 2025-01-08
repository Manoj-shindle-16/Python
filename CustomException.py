import re
class InvalidUsernameError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass
un=0
pw=0
def validation():
    global un
    global pw
    un = int(input("Enter the Username.. : "))
    if re.search(r"[A-Za-z_]+",un) and len(un)<=15:
        pw = int(input("Enter Password.. : "))
        if re.search(r"[A-Za-z_]+",pw) and re.search(r"\W+",pw) and re.search(r"\d+",pw) and len(pw)>=8:
            print("You Entered Valid Credentials..")
        else:
            print("Enter Valid Password...!!")
            raise InvalidPasswordError("Provide Password using (atleast 1 camelCase letter,1 special symbol and number.. )")
    else:
        print("Enter Valid UserName...!!!")
        raise InvalidUsernameError("Provide Username using alphabets and underscore..")
try:
    validation()
except:
    print("Wrong Credential..")
    print("You have 2 more chances..")
    try:
        validation()
    except:
        print("You have last one chance..!")
        try:
            validation()
        except:
            print("Contact Customer Service..")
    
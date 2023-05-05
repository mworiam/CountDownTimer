import string

def password_check():
    my_password = input("Enter your password: ")

    my_password_list = list(my_password)

    qualifications = ["lowercase", "uppercase", "digits", "special characters"]

    for letters in my_password_list:
        if letters in string.ascii_lowercase:
            if "lowercase" in qualifications:
                qualifications.remove("lowercase")
        elif letters in string.ascii_uppercase:
            if "uppercase" in qualifications:
                qualifications.remove("uppercase")
        elif letters in string.digits:
            if "digits" in qualifications:
                qualifications.remove("digits")
        else:
            if "special characters" in qualifications:
                qualifications.remove("special characters")

    if len(qualifications) == 0 and len(qualifications) > 9:
        print("Password is strong")

    if len(my_password_list) <=9:
        print("Password is too short, must be atleast 9 characters")

    if len(qualifications) != 0:
        print("Password too weak, following condition hasn't been met: " + ", ".join(qualifications))

password_check()
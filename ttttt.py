password = input()
is_long_enough = len(password) >=8
is_alphanumeric = password.isalnum()
if is_long_enough and is_alphanumeric:
    print("True")
else:
    print("False")
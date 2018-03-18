correctPassword = "123"

name = input("Enter name: ")
password = input("Enter password: ")

while correctPassword != password:
    password = input("Wrong password! Enter again: ")

print ("Hi %s you are logged in" % name)

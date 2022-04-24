import random
import string
char = list(string.ascii_letters+string.digits+"!@#$%^&*()-=[]{}|")
lenght = int(input("Enter the Lenght Do U Want: "))
Amount = int(input("Enter the How Many Passwd Do U Want: "))
c = input("enter the Passwrd / 0 for no change: ")
for x in range(Amount):
    passwd = ("".join(random.sample(char, lenght)))
    if c==0:
        print(passwd)
    else:
        print(c+passwd)

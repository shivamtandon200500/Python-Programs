import random
import pyautogui
import string
l=[]
# chars="abcdefghijklmnopqrst0123456789"
# chars="abcdefghijklmnopqrstuvwxyz"
chars=string.printable
chars_list=list(chars)
password=pyautogui.password("Enter a password : ")

guess_password=""

# while(guess_password!=password):
#     guess_password=random.choices(chars_list,k=len(password))
#
#     print("<=================="+str(guess_password)+"==================>")
#
#     if guess_password==list(password):
#         print("Your password is : "+"".join(guess_password))
#         break

def search(g,p):
    while (True):
        g = random.choice(chars_list)
        print("<==================" + str(g) + "==================>")

        if g==p:
            return g
            break
for p in password:
    l.append(search(guess_password,p))
    guess_password=""
final=''.join(l)
if final==password:
     print("Your password is :", final)
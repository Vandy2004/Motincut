import math as m
import random as r
def password_generate():
     string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%^&*"'
     password=" "
     password_length=len(string)  
     for i in range(length_password):
        password+=string[m.floor(r.random()*password_length)]
     return(password)
length_password=int(input("Enter the length of password:"))
no_of_passwords=int(input("Enter the number of passwords to generate:"))
temp=no_of_passwords
while(no_of_passwords>0): 
  print("Your One Time Password is",password_generate())
  no_of_passwords-=1
print(temp,"PASSWORDS WERE GENERTAED SUCCESSFULLY")

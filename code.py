# Password-Generation
#User enter the lenght of the password  and random strong password will be generated with alphabets ,numbers and special character. 
"""
Create a program that takes the length of the password as input and generates a random password of the same length. The strength of the password 
depends equally on the 4 properties mentioned below. If the password generated randomly following the rules or constraints given below, then that password is treated as good in terms of strength and accepted otherwise ignore that password.
The properties to be followed for a strong password are:
•	At least 12 characters.
•	A mixture of both uppercase and lowercase letters.
•	A mixture of letters and numbers. 
•	Inclusion of at least one special character, e.g., @ #?]

"""
import random
l=int(input("Enter the Lenght of the Password: "))
s=""
x=["~","!","@","#","$","%","^","&","*"]
z=[1,2,3,4,5,6,7,8,9,0]
y=[]
for i in range(65,91):
    y.append(chr(i))
for i in range(97,123):
    y.append(chr(i))
if l>=12:
    for i in range(l):
        a=random.randint(1,3)
        if a==1:
            b=random.randint(0,51)
            s+=y[b]
        elif a==2:a
            b=random.randint(0,9)
            s+=str(z[b])
        elif a==3:
            b=random.randint(0,8)
            s+=x[b]
    print("The generated password is :",s)
    
else:
    print("Your password should have atleast 12 character")

            
        

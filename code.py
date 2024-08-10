# Password-Generation

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

            
        

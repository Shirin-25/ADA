def hcf(a,b):
    while b!=0:
        a,b= b,a%b
    return a

a=int(input("enter the  low num"))
b=int(input("enter the high  num:"))
print("the hcf is:",hcf(a,b))
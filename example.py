x=float(input("gross salary : "))
a=float(input("enter deduction : "))
w=x-(x*a/100)
b=float(input("enter deduction : "))
p=x-(x*b/100)
c=float(input("enter deduction : "))
q=x-(x*c/100)
r=w+p+q
print(4*(x-r))

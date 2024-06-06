a = float(input("what is the value of a? "))
b = float(input("what is the value of b? "))
c = float(input("what is the value of c? "))

D = b**2-4*a*c
if D>0 and a!=0:
    print((-b+(D)**0.5)/2*a , (-b-(D)**0.5)/2*a)
elif D==0 and a!=0:
    print((-b / 2 * a), (-b / 2 * a))
elif D<0 and a!=0:
    print("no real roots")
else :
    print("not a valid quadratic equation")

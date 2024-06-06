a = float(input("what is the value of a? "))
b = float(input("what is the value of b? "))

print(a+b)
print(a-b)
print(a*b)
if b==0:
    print("cannot be divided")
else:
    division = a/b
    print(division)
print(a**b)
print((a**2+b**2)**0.5)
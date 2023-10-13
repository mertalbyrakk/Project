# Delta = b^2 -4 a.c
# Denklem kök bulma x1 = -b+DELTA**0.5/2*a

print("Denklemin baş kat sayılarını yazın")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print("Denkleminiz:")
print(int(a),"x^2+",int(b),"x+",int(c),sep="" )

delta = b**2 -4*a*c

print("Denkleminiz kökleri")

x1 = (-b -delta**0.5)/(2*a)
x2 = (-b +delta**0.5)/(2*a)

print(x1)
print(x2)
'''
# For int
x = input("x: ")
y = input("y: ")

z = int(x) + int(y)

print(z)

#for float (decimal)
x = input("x: ")
y = input("y: ")

z = float(x) + float(y)

print(z)


x = float(input("x: "))
y = float(input("y: "))

z = round(x + y)

print(f"{z:,}")



x = float(input("x: "))
y = float(input("y: "))

z = round(x / y, 2)

print(z)



x = float(input("x: "))
y = float(input("y: "))

z = x / y

print(f"{z:.2f}")
'''

def main():
    x = int(input("x: "))
    print("x squared is", square(x))


def square(n):
    return pow(n,n)
main()
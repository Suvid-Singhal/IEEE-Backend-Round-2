#Using Euclidean Algorithm
def gcd(x,y):
    while y:
        x,y=y,x%y
    return abs(x)

one=int(input("Enter number 1: "))
two=int(input("Enter number 2: "))
three=int(input("Enter number 3: "))
four=int(input("Enter number 4: "))
five=int(input("Enter number 5: "))
print("GCD of the given numbers is ",gcd(one,gcd(two,gcd(three,gcd(four,five)))))

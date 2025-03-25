def sum_product(a,b):
    return a+b,a*b

x=int(input("enter first number:"))
y=int(input("enter second number:"))
sum,product = sum_product(x,y)
print("sum of two numbers is ", sum)
print("oroduct of two numbers is", product)


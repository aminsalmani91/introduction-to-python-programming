def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y

a=int(input("please enter a number = "))
b=int(input("please enter a number = "))

print(swap(a,b))

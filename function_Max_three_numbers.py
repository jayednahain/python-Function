def max_of_two( x, y,z ):
    if x>y>z:
        return print("big value is: ",x)
    elif y>x>z:
        return print("big value is: ",y)
    else:
        return print("big values is: ",z)

a=int(input("value one: "))
b=int(input("value two: "))
c=int(input("value three: "))


max_of_two(a,b,c)

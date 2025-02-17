def total_sum(a:float,b:float,*args)->float:
    values = [a,b]+list(args)
    return sum(values)

def average(a:float,b:float,*args)->float:
    return total_sum(a,b,*args)/(len(args)+2)

a = float(input("enter with the value of a:"))
b = float(input("enter with the value of b:"))
c = float(input("enter with the value of c:"))
d = float(input("enter with the value of d:"))

print("average",average(a,b,c,d))
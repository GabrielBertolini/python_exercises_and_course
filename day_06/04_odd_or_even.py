def odd_even(number: int):
    if number % 2 == 0:
       return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))

result=odd_even(number)

print("the number",number,"is",result)
import random

def get_input():
        while True:
            try:
                user_number=int(input("enter a number: "))

            except ValueError as err:
                 print("Invalid value!")
                 continue
            
            if 1<=user_number<=15:
                 return user_number
            
            print("Invalid value! The number must be between 1 and 15")

def check_number(draw,user):
     if draw==user:
          print("Congratulations! You are now a millionaire!")
          return True
     
     elif user>draw:
          print("Your number is too high! Select a smaller one!")

     else:
        print("Your number is too low! Select a bigger one!")
        return False


draw_number=random.randint(1,15)

for i in range(3):
    user_number = get_input()
    if check_number(draw=draw_number, user=user_number):
        break 

else:
    print("Your attempts are over! The correct number was:", draw_number)
     
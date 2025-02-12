total_seconds=int(input("type the number of seconds"))

hours=total_seconds//3600 #1hr has 3600s
minutes=(total_seconds%3600)//60 # remainder of s after hr
seconds=total_seconds%60 # remainder of s after min

#the total time is
print(f"{hours}:{minutes:02d}:{seconds:02d}")
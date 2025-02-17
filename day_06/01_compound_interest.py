# %%

def compound_interest(contribuition:int, interest_rate:float ,years:int)->float:

 """compound_interest is used to calculate the rate of an investment considering the interest rate and time

  contribuition:
    a whole number that represents your investment amount in $
 
interest_rate:
    a float number between 0 and 1 that represents your interest rate
 
 years:
    a whole number >=1 that representshow many years you invested"""
    
 return contribuition*(1+interest_rate)**years
# %%
print(compound_interest(contribuition=1000, interest_rate=0.13, years=4))
value=compound_interest(contribuition=1000, interest_rate=0.13, years=4)
type(value)

# %%


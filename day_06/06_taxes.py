
def tax_amount(price:float,tax_rate:float,**kwargs):
    total_tax = price*tax_rate
    for i in kwargs:
        print(i,kwargs[i])
        total_tax+=price*kwargs[i]
    
    return total_tax

all_taxes= {
    "city_tax":0.01,
    "state_tax":0.005,
    "federal_tax":0.0001
}

tax_amount(100, 0.03,**all_taxes, internacional=0.002)
#tax_amount(100, 0.03,city_tax=0.01,state_tax=0.005,federal_tax=0.0001)
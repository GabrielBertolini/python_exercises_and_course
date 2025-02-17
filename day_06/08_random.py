# %%
import random
import datetime

# %%
random.randint(1,10)
# %%

x=["Gabriel","Carol","Ana"]
random.choice(x)
# %%

x = [1, 2, 3, 4, 5]
random.seed(datetime.datetime.now().timestamp())
random.choices(x, k=2) 

# %%
## sampling without replacemen
names=["Gabriel","Carol","Ana"]

value_1=random.choice(names)

names.remove(value_1)

value_2=random.choice(names)

names

# %%

# Shop
stock1 = "chocolate mint"
stock2 = "vanilla"
stock3 = "coffee"
stock4 = "green tea"

# Expected Output
# Yes, we have vanilla in stock

# Sorry, we ran out strawberry
 
#  case1:
order = input("What kind of icecream do you want ?").lower()

if order in (stock1,stock2,stock3,stock4):
    print(f"Yse, we have {order} in stock") 
else:
    print(f"Sorry, we ran out {order}")



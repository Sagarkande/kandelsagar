name = input("what is your name:")
sales_amt = float(input("please insert the amount of sales"))
if sales_amt >=50000:
    bonus= 500.0
    print(f"congratulations dear {name}, You have received {bonus} as a bonus")
else:
    print("you did not received bonus")
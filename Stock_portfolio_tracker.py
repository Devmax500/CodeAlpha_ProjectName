# CodeAlpha Internship Task 2
print("Welcome to the stock portfolio tracker!")
stocks = {"AAPL": 175.25,
    "MSFT": 430.10,
    "GOOGL": 150.50,
    "AMZN": 185.70,
    "NVDA": 118.90}

print(stocks)

user_stock_portfolio = {}

# Accepts users stock choice:
user_stock_choice = input("Enter the stock name you will like to invest in!:")

# Checks if users stock choice is in the list of stocks available
if user_stock_choice in stocks.keys():
  user_stock_amount = int(input("Enter the amount you'd like to buy:"))
  user_stock_portfolio.update({user_stock_choice : user_stock_amount * stocks[user_stock_choice]})
  print(user_stock_portfolio)
  for stocks, amount in user_stock_portfolio.items():
    with open(r'Code Alpha Internship Tasks/stock_portfolio.txt', mode='w') as f:
      f.write(f"{stocks}\t")
      f.write(str(amount))
else:
    print("You've got a wrong stock entry.")
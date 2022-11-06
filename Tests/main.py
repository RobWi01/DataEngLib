import os

# Import the created library
from MainFuncLib import main

# Import Portfolio class
from Tests.Classes import Portfolio

if os.path.lexists("./sqlite/final.db"):
    os.remove("./sqlite/final.db")

currency_pairs = [["AUD", "USD", [], Portfolio.Portfolio("AUD", "USD")],
                  ["GBP", "EUR", [], Portfolio.Portfolio("GBP", "EUR")]]

result = main(currency_pairs)

#Check if the main function ran
assert result == None

# Add some more unit tests here
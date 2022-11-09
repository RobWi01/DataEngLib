# Run this file to check if the library runs the code correctly, once the key issue is resolved
# more unit tests can be added to test if the final database is created correctly.

import os

# Import the created library
from MainFuncLib import mainFunc

# Import Portfolio class
from Tests.Classes import Portfolio

if os.path.lexists("./sqlite/final.db"):
    os.remove("./sqlite/final.db")

# I use two currencies to test
currency_pairs = [["AUD", "USD", [], Portfolio.Portfolio("AUD", "USD")],
                  ["GBP", "EUR", [], Portfolio.Portfolio("GBP", "EUR")]]

result = mainFunc(currency_pairs)

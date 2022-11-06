# Medium multiply
Add more documentation here

### Installation
```
pip install MainFuncLib
```

### Get started
How to use this library in Max's code:

```Python
from MainFuncLib import main


# Example with 2 currency pairs
currency_pairs = [["AUD", "USD", [], Portfolio.Portfolio("AUD", "USD")],
                  ["GBP", "EUR", [], Portfolio.Portfolio("GBP", "EUR")]]

main(currency_pairs)
```
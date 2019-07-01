# You are given the current stock prices.
# You have to find out which stocks cost more.
#
# Input: The dictionary where the market identifier code
# is a key and the value is a stock price.
#
# Output: A string and the market identifier code.
#
# Preconditions: All the prices are unique.

# interesting:
# max(data) returns key with first letter closest to Z
# min(data) does opposite
def best_stock(data):
    stock_list = []
    for company in data:
        stock_value = data[company]
        stock_list.append(stock_value)
    max_stock = max(stock_list)
    for company,stock_value in data.items():
        if stock_value == max_stock:
            return company
data = {'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2,
        'YAG': 400.1,}

print(best_stock(data))


# BETTER
#    for k, v in data.items():
#         if v == (max(data.values())):
#             return k


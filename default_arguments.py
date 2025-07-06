# Default Arguments = A default value for certain parameters
#                     Default is used when that argument is omitted
#                     make youe function more flexible , reduce # of arguments
#                     1. positional, 2. Default, 3. Keyword, 4. Arbitrary

def net_price (list_price, discount = 0, tax = 0.05):
    return list_price * (1-discount) * (1+tax)

# print(net_price(500))
# print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

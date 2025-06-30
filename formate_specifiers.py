# formate specifiers = {value:flags} formate a value based on what flags are inserted.

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := => place sign to leftmost position
# : => insert a space before positive numbers
# :, => comma separator

price1 = 30006516.752
price2 = -35874656.852
price3 = 30035456.652

print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")
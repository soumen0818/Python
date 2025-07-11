# nested loop => A loop within another loop (outer, inner)
#                outer loop:
#                      inner loop:


rows = int(input("Enter the no. of rows : "))
columns = int(input("Enter the no. of rows : "))
symbol = input("Enter a symbol to use : ")


for x in range (rows):
    for y in range (columns):
        print(symbol, end="")
    print()
    

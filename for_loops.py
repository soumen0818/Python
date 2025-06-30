# for looop = Execute a block of code a fixed number of times.
#             you can iterate over a range , string, sequence, etc.

for x in reversed(range (1,11)):
    print(x)

# 1. Python For Loop with String  

name = "soumen"
for x in name :
    print(x)
    
# 2. Using range() with For Loop  => range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

for x in range (1,20,2):
    print(x)

# 3. Continue & Break with For Loop

phone_number = "9339982624"
for x in phone_number :
    if x == "8":
        # continue 
        break  
    print(x)



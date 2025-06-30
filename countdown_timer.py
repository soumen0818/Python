import time

my_time = int (input ("Enter the time in seconds : "))
for x in range (my_time, 0, -1):
    seconds = x % 60
    minuetes = int (x / 60) % 60
    hour = int (x / 3600)
    print(f"{hour:02} : {minuetes:02} : {seconds:02}")
    time.sleep(1)
    
print("Times up !")
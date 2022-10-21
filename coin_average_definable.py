import random

# this program gets random numbers (you can change how many random numbers is going to used in program by changeing "coins")
# which might be 0 or 1 and then it checks all numbers until they are all ones(1) also it does the same
# process for given numbers in the trys value. And at the end it prints the average value of how
# many trys needed to get all random numbers as 1. (This is a modified version of the program which shows the progress
# by printing which try is executed currently.)

coins = 3
total = 0
mylist = []
winlist = []
trys = 1000

for x in range(trys):
    win = 0
    scr = 1
    while win == 0:
        for i in range(coins):
            winlist.append(random.randint(0,1))
        if (sum(winlist) == coins):
            print(f"currently at try:{x}")
            win = 1
            mylist.append(scr)
            winlist.clear()
        else:
            # print("you lost", scr)
            win = 0
            scr = scr + 1
            winlist.clear()
total_math = round(sum(mylist)/len(mylist))
print("Result is:", total_math)

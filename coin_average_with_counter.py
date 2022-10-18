import random

# this program gets 8 random numbers which might be 0 or 1 and then it checks all numbers until they are all ones(1)
# also it does the same process for given numbers in the trys value. And at the end it prints the average value of how
# many trys needed to get all random numbers as 1. (This is a modified version of the program which shows the progress
# by printing which try is executed currently.)

total = 0
mylist = []
trys = 10000

for x in range(trys):
    win = 0
    scr = 1
    while win == 0:
        a = random.randint(0,1)
        b = random.randint(0,1)
        c = random.randint(0,1)
        d = random.randint(0,1)
        e = random.randint(0,1)
        f = random.randint(0,1)
        g = random.randint(0,1)
        h = random.randint(0,1)
        if a == 1 and b == 1 and c == 1 and d == 1 and e == 1 and f == 1 and g == 1 and h == 1:
            # print("you won", scr)
            print(f"currently at try:{x}")
            win = 1
            mylist.append(scr)
        else:
            # print("you lost", scr)
            win = 0
            scr = scr + 1
    # print(x)
    # print(mylist)

total_math = round(sum(mylist)/len(mylist))
print("Result is:", total_math)

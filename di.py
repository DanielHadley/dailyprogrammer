# Simulate 10 - 10k rolls of a fair di
# http://www.reddit.com/r/dailyprogrammer/comments/25y2d0/5192014_challenge_163_easy_probability/

import random
 
di = range(1,7)
 
def roll(n):
    rolls = [ ]
    for i in range(0,n):
        i = random.choice(di)
        rolls.append(i)
    return rolls


def prob(rolls):
    for s in di:
        p = rolls.count(s) / float(len(rolls))
        print ('{:.2%}'.format(p)), 

testThese = (10,100,1000,10000)

header = "# of Rolls 1s     2s     3s     4s     5s     6s    "
print(header)
print("="*len(header))

for t in testThese:
    print t,(" ".ljust(8-len(str(t)), ' ')), (prob(roll(t)))



RAW = """16,1,2,0,4,2,7,1,2,14"""

with open('./data/day07.txt') as f:
    raw_inp = f.read()

# Use test data
# raw_inp = RAW

# parse input
crabpos = [x for x in map(int,raw_inp.split(','))]

# calculate x* with secant method
crabpos.sort()

def f(x):
    # do sgn part
    n = len(crabpos)
    sgn_sum = 0
    for c in crabpos:
        if c - x > 0:
            sgn_sum += 1
        elif c - x < 0:
            sgn_sum -= 1

    mean = sum(crabpos)/n

    return sgn_sum/(2*n) + mean - x

# init secant
delta = 9999
x0 = crabpos[0]
x1 = crabpos[-1]
while delta > 0.2:
    xnew = x1 - ((x1-x0)*f(x1))/(f(x1) - f(x0))
    delta = abs(xnew-x1)
    x0 = x1
    x1 = xnew

xstar = round(x1)

print(xstar)

# get distances from xstar and sum together
dist = 0
for x in crabpos:
    dist += (abs(x-xstar)**2 + abs(x-xstar))/2

print(dist)
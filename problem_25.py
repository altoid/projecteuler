#!/usr/bin/env python

# first fibonacci # with 1000 digits

def fib():
    n1 = 1
    n2 = 1

    yield n2
    yield n1

    while True:
        n = n1 + n2
        yield n

        n2 = n1
        n1 = n

digits = 1000
threshold = 10 ** (digits - 1) - 1
answer = 0

c = 0
for f in fib():
    if f > threshold:
        answer = f
        break

#    print f, c
    c += 1

print len(str(answer)), c

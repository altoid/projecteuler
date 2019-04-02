#!/usr/bin/env python

def producttcudorp():
    result = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            p = i * j
            s = str(p)
            if s == s[::-1]:
                if p > result:
                    result = p
                    print i, j, p

if __name__ == '__main__':
    producttcudorp()


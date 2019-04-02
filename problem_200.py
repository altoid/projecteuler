primes = [2, 3, 5, 7, 11, 13, 17, 19]

def sqube(p, q):
    return (p ** 2) * (q ** 3)

def main():
    global primes
    nprimes = len(primes)

    # maintain sq1 < cb1
    sq1 = 0
    cb1 = 1

    # maintain cb2 < sq2
    cb2 = 0
    sq2 = 1

    while cb1 + 1 < nprimes and sq2 + 1 < nprimes:

        term1 = sqube(primes[sq1], primes[cb1])
        term2 = sqube(primes[sq2], primes[cb2])
    
        terms = [term1, term2]
        print terms
        result = min(terms)

        if result == term1:
            print "sqube(%d, %d) = %d" % (
                primes[sq1], primes[cb1],
                result)
        else:
            print "sqube(%d, %d) = %d" % (
                primes[sq2], primes[cb2],
                result)
    
        # which do we increment?

        a = b = c = d = None
        terms = []

        if sq1 + 1 < cb1:
            a = sqube(primes[sq1 + 1], primes[cb1])
            terms.append(a)

        b = sqube(primes[sq1], primes[cb1 + 1])
        terms.append(b)

        c = sqube(primes[sq2 + 1], primes[cb2])
        terms.append(c)

        if cb2 + 1 < sq1:
            d = sqube(primes[sq2], primes[cb2 + 1])
            terms.append(d)

        result = min(terms)
        if result == a:
            sq1 += 1
            print "1: sqube(%d, %d) = %d" % (
                primes[sq1], primes[cb1],
                result)
        elif result == b:
            cb1 += 1
            print "2: sqube(%d, %d) = %d" % (
                primes[sq1], primes[cb1],
                result)
        elif result == c:
            sq2 += 1
            print "3: sqube(%d, %d) = %d" % (
                primes[sq2], primes[cb2],
                result)
        else:
            cb2 += 1
            print "4: sqube(%d, %d) = %d" % (
                primes[sq2], primes[cb2],
                result)


if __name__ == '__main__':

    main()



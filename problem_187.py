import util
import math

def semiprimes(top):
    # get all the primes <= top/2
    # for each i in primes
    #     for each j in primes >= i
    #         result = i * j
    #         if result >= top:
    #             break
    meh, primes = util.sieve(top // 2)
    nprimes = len(primes)

    answer = 0
    c0 = 0
    while c0 < nprimes:
        c1 = c0
        if primes[c0] * primes[c1] >= top:
            break

        while c1 < nprimes:
            if primes[c0] * primes[c1] >= top:
                break
#            print "%d * %d = %d" % (
#                primes[c0], primes[c1], primes[c0] * primes[c1])

            answer += 1
            c1 += 1
        c0 += 1

    return answer

if __name__ == '__main__':
    answer = semiprimes(10 ** 8)
#    answer = semiprimes(3000)
    print "answer:", answer




#!/usr/bin/python3

'''Define function'''


def isWinner(x, nums):
    '''Winner'''
    def sieve(n):
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n) if primes[p]]

    def play_game(n):
        primes = sieve(n)
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

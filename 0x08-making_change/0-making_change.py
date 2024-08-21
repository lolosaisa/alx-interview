#!/usr/bin/python3



def makeChange(coins, total):
    memo = {}

    #there is only one way to find no of coins for total 0
    memo[0] = 1

    for i in range(1, total+1):
        memo[1] = 0

        #check the solution of previous coin by checking each coin denomination
        for coin in coins:
            subproblem = i - coin

            #if your solution is negative, meaning we cant use the coin but if it is positive we can use it
            if subproblem >= 0:
                memo[i] += memo[subproblem]

 return memo[total]



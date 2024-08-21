#!/usr/bin/python3
""" function to get the fewest coins to make change"""

def makeChange(coins, total):
    #using bottom up, initially our array can hold the largest possible value
    memo = [float('inf')]* (total+1)
    
    #we need 0 coins to make the total of 0
    memo[0] = 0
    
    #we loop through each amount from 1 to total
    for i in range(1, total +1):
        #we ae going to chechk the previous solution/ coin denomination
        for coin in coins:
            if i - coin >= 0:
                memo[i] = min(memo[i], memo[i-coin] + 1)
                
    #if memo[total] is infinity it means it is an impossible task            
    return memo[total] if memo[total] != float('inf')else -1